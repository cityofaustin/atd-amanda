"""
Create a prioritized list of right-of-way (ROW) permits to be
inspected based on various scoring criteria.

TODO:
Remove brackets from zone column when writing to CSV
"""
import csv
import pdb

import agolutil
import arcgis

from config.config import (
    PERMITS_FILE,
    SEMGENTS_FILE,
    OUTPUT_FILE,
    FIELD_CFG,
    SEGMENT_LAYER_CFG,
    DAPCZ_SEGMENTS,
    INSPECTOR_LAYER_CFG,
)

from config.secrets import AGOL_CREDENTIALS


def get_total_scores(permits, score_keys):
    for permit_id in permits.keys():
        score = 0

        for key in score_keys:
            try:
                score += permits[permit_id][key]
            except:
                # TODO: why though?
                continue

        permits[permit_id]["total_score"] = score

    return permits


def score_permits_by_road_class(permits, source_key, score_key):
    """
    Our score criteria: Critical = 10, Arterial = 7, Collector = 5, Residential = 3

    1, 2, 4 =  10 (Interstate, US and State Highways, Major Arterials)
    5 = 7 (Minor arterials)
    8 = 5 (city collector)
    else = 3 (local city/county streets, whatever else)
    
    ### CTM GIS Street Segment Road Classes
    1   A10 Interstate, Fwy, Expy
    2   A20 US and State Highways
    4   A30 Major Arterials and County Roads (FM)
    5   A31 Minor Arterials
    6   A40 Local City/County Street
    8   A45 City Collector
    9   A61 Cul-de-sac
    10  A63 Ramps and Turnarounds
    11  A73 Alley
    12  A74 Driveway
    13  ROW Jurisdiction Border Segment
    14  A50 Unimporoved Public Road
    15  A60 Private Road
    16  A70 Routing Driveway/Service Road
    17  A72 Platted ROW/Unbuilt
    53  A25 (Not used - Old SH)
    57  A41 (Not used - Old Collector)
    """

    for permit_id in permits.keys():
        road_classes = permits[permit_id].get("road_classes")

        if any(road_class in [1, 2, 4] for road_class in road_classes):
            # Interstate, US and State Highways, Major Arterials
            permits[permit_id][score_key] = 10

        elif any(road_class == 5 for road_class in road_classes):
            # Minor arterials
            permits[permit_id][score_key] = 7

        elif any(road_class == 8 for road_class in road_classes):
            # Collector
            permits[permit_id][score_key] = 5

        else:
            permits[permit_id][score_key] = 3

    return permits


def score_dapcz_segments(permits, dapcz_segments):
    # weight street segments that are in the Downtown Area Project Cooridnation Zone (DAPCZ)
    for permit_id in permits.keys():
        segment_ids = permits[permit_id].get("street_segments")

        if segment_ids:
            for segment_id in segment_ids:
                if segment_id in dapcz_segments:
                    permits[permit_id]["dapcz_score"] = 10
                    break

                else:
                    permits[permit_id]["dapcz_score"] = 0
    return permits


def stringify_list(permits, key):
    # turn insepctor zone arrays into plain comma-separates strings
    for permit_id in permits.keys():
        zone_array = permits[permit_id].get(key)
        if zone_array:
            permits[permit_id][key] = ", ".join(str(x) for x in zone_array)
        else:
            permits[permit_id][key] = ""
    
    return permits


def merge_inspector_zones(
    permits, segments_with_inspector_zones, key="inspector_zones"
):
    """
    Join inspector zone data from GIS lookup to master permits object
    """
    for permit_id in permits.keys():

        permits[permit_id]["inspector_zones"] = []

        segments = permits[permit_id].get("street_segments")

        if not segments:
            continue

        for segment_id in segments:
            segment_data = segments_with_inspector_zones.get(
                int(segment_id)
            )  # < segment_id in permits object is a string!

            if not segment_data:
                continue

            inspector_zones = segment_data.get("inspector_zones")

            if not inspector_zones:
                continue

            for zone in inspector_zones:
                permits[permit_id]["inspector_zones"].append(zone)

                # remove duplicate zones for each permit
                permits[permit_id]["inspector_zones"] = list(set(permits[permit_id]["inspector_zones"]))

    return permits


def get_max_road_class(permits, road_class_segments):
    for permit_id in permits.keys():
        segments = permits[permit_id].get("street_segments")

        road_classes = []

        if segments:

            for segment_id in segments:

                segment_id = int(segment_id)

                if segment_id in road_class_segments:
                    road_classes.append(road_class_segments[segment_id]["road_class"])

        permits[permit_id]["road_classes"] = road_classes

    return permits


def get_inspector_areas(
    segment_features,
    inspector_layer,
    inspector_layer_cfg,
    segment_id_field="SEGMENT_ID",
    inspector_zone_id_field="ROW_INSPECTOR_ZONE_ID",
):

    segments_with_zones = {}

    sr = segment_features.spatial_reference

    max_retries = 5

    for feature in segment_features:
        n = 0
        # add segment geometry to params, which is passed to interesect request
        # inspector_layer_cfg["params"]["geometry"] = feature.geometry
        segment_id = feature.attributes[segment_id_field]
        segments_with_zones[segment_id] = {"inspector_zones": []}

        geom = feature.geometry

        filter_ = arcgis.geometry.filters.intersects(sr=sr, geometry=geom)

        while True:
            try:
                intersect_zones = inspector_layer.query(
                    geometry_filter=filter_, return_geometry=False
                )

            except Exception as e:
                n += 1
                if n == max_retries:
                    raise e
            break

        for zone in intersect_zones:
            segments_with_zones[segment_id]["inspector_zones"].append(
                zone.attributes[inspector_zone_id_field]
            )

    return segments_with_zones


def parse_road_class(segment_features, segment_id_key, road_class_id_key="ROAD_CLASS"):
    segments_with_road_class = {}

    for feature in segment_features:
        segment_id = feature.attributes[segment_id_key]
        road_class = feature.attributes[road_class_id_key]
        segments_with_road_class[segment_id] = {"road_class": road_class}

    return segments_with_road_class


def get_segment_data(segment_ids, segment_layer, layer_cfg):
    print("get segment data")
    # ready id string as a sql-like statement
    where_ids = ", ".join(f"'{x}'" for x in segment_ids)

    where = "{} in ({})".format(layer_cfg["primary_key"], where_ids)

    features = segment_layer.query(
        where=where, outFields=layer_cfg["outfields"], returnGeometry=True
    )

    return features


def get_all_score_keys(config):
    score_keys = []

    for key in config:
        score_key = config[key].get("score_key")
        if score_key:
            score_keys.append(score_key)

    return score_keys


def total_score(permits, score_keys, total_score_key_name="total_score"):
    return permits


def score_permits_by_duration(
    permits,
    duration_key=FIELD_CFG["duration"]["source_key"],
    score_key=FIELD_CFG["duration"]["score_key"],
):
    print("score by duration")

    for permit_id in permits:

        try:
            duration = int(permits[permit_id][duration_key])
        except ValueError:
            # TODO: how to handle permits with duration?
            duration = 999

        if duration <= 6:
            score = 10
        elif duration <= 15:
            score = 5
        elif duration <= 30:
            score = 3
        else:
            score = 1

        permits[permit_id][score_key] = score

    return permits


def append_key(primary, append_dict, append_key):
    """
    primary: dict that will receive the new key
    append_dict: dict that contains the data that will be appended
      to the primary
    append_key: the key/value that will be added to the primary
    """

    for record_id in append_dict:
        try:
            primary[record_id][append_key] = append_dict[record_id][append_key]
        except KeyError:
            # TODO: why is the key missing?
            continue

    return primary


def score_permits_by_segment_count(
    permits, count_key="segment_count", score_key=FIELD_CFG["street_segments"]["score_key"]
):
    print("score by segment count")
    for permit_id in permits:
        count = permits[permit_id][count_key]

        if count > 1:
            permits[permit_id][score_key] = 10
        if count <= 1:
            permits[permit_id][score_key] = 5

    return permits


def segments_by_permit(segments):
    # count the number of segments per permit
    # return a dict of permit ID with count of segments and list of segment ids
    permit_segments = {}

    for seg in segments:
        # FOLDERRSN is the unique permit identifer
        permit_id = seg.get("FOLDERRSN")

        if permit_id not in permit_segments:
            permit_segments[permit_id] = {"segment_count": 0}
            permit_segments[permit_id]["street_segments"] = []

        permit_segments[permit_id]["segment_count"] += 1
        permit_segments[permit_id]["street_segments"].append(seg.get("PROPERTYID"))

    return permit_segments


def index_by_key(list_of_dicts, key):
    # transform a list of dicts into a dict with a top-level index
    return {row[key]: row for row in list_of_dicts}


def main():
    # just reading all the data into memory
    # because we expect < 1mb of data

    with open(PERMITS_FILE, "r") as fin:
        reader = csv.DictReader(fin)

        permits = [row for row in reader]
        permits = index_by_key(permits, "PERMIT_RSN")

    with open(SEMGENTS_FILE, "r") as fin:
        reader = csv.DictReader(fin)

        segments = [row for row in reader]

    # **number of segment scoring**
    permits_with_segments = segments_by_permit(segments)

    permits_weighted_with_seg_count = score_permits_by_segment_count(
        permits_with_segments
    )

    # join segment weight to permits
    permits = append_key(
        permits, permits_weighted_with_seg_count, FIELD_CFG["street_segments"]["score_key"]
    )

    # join segment id list to permits
    permits = append_key(permits, permits_with_segments, "street_segments")
    
    # **duration scoring**
    permits = score_permits_by_duration(permits)

    # **segment road class scoring**

    segment_ids = [
        segment[FIELD_CFG["street_segments"]["segment_id_key"]] for segment in segments
    ]

    # remove dupes
    segment_ids = list(set(segment_ids))

    # query segment data from ArcGIS Online in chunks
    chunksize = 500

    segment_features = []

    segments_with_zones = {}

    # get arcgis feature layers
    segment_layer = agolutil.get_item(
        auth=AGOL_CREDENTIALS,
        service_id=SEGMENT_LAYER_CFG["service_id"],
        layer_id=SEGMENT_LAYER_CFG["layer_id"],
    )

    inspector_layer = agolutil.get_item(
        auth=AGOL_CREDENTIALS,
        service_id=INSPECTOR_LAYER_CFG["service_id"],
        layer_id=INSPECTOR_LAYER_CFG["layer_id"],
    )

    segments_with_road_class = {}
    segments_with_zones = {}
    segments_with_zones_and_road_class = {}

    for i in range(0, len(segment_ids), chunksize):
        # get road class
        segment_features_subset = get_segment_data(
            segment_ids[i : i + chunksize], segment_layer, SEGMENT_LAYER_CFG
        )

        segments_with_road_class_subset = parse_road_class(
            segment_features_subset, SEGMENT_LAYER_CFG["primary_key"]
        )

        segments_with_road_class.update(segments_with_road_class_subset)

        # get inspector area via intersect query
        segment_with_zones_subset = get_inspector_areas(
            segment_features_subset, inspector_layer, INSPECTOR_LAYER_CFG
        )

        segments_with_zones.update(segment_with_zones_subset)

    # merge zones and road class data
    for key in segments_with_zones:
        segments_with_zones_and_road_class[key] = {}

        segments_with_zones_and_road_class[key][
            "inspector_zones"
        ] = segments_with_zones[key]["inspector_zones"]

        segments_with_zones_and_road_class[key][
            "road_class"
        ] = segments_with_road_class[key]["road_class"]

    # TODO
    # only doing small chunks now
    # fix this to play with segments_with_zones_and_road_class
    # segment_road_class = index_by_key(segment_road_class, SEGMENT_LAYER_CFG["primary_key"])

    permits = get_max_road_class(permits, segments_with_zones_and_road_class)

    permits = score_permits_by_road_class(
        permits,
        FIELD_CFG["road_classes"]["source_key"],
        FIELD_CFG["road_classes"]["score_key"],
    )

    # add inspector zones to permits dict
    permits = merge_inspector_zones(permits, segments_with_zones_and_road_class)
    
    # **score DAPCZ segments**
    permits = score_dapcz_segments(permits, DAPCZ_SEGMENTS)

    permits = stringify_list(permits, "inspector_zones")
    
    permits = stringify_list(permits, "road_classes")

    permits = stringify_list(permits, "street_segments")

    # **total up the score
    score_keys = get_all_score_keys(FIELD_CFG)

    permits = get_total_scores(permits, score_keys)

    # **write to csv**
    output_data = [permits[permit_id] for permit_id in permits.keys()]

    with open(OUTPUT_FILE, "w") as fout:
        # assume fieldnames are consistent across all records,
        # so just take the keys from the first entry as fieldnames
        writer = csv.DictWriter(fout, fieldnames=output_data[0].keys())

        writer.writeheader()

        for row in output_data:
            writer.writerow(row)


results = main()

# sort the dicts by seg vals
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# results = sorted(results.items(), key=lambda kv: kv[1], reverse=True)
