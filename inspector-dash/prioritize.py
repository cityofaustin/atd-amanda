# TODO
# Roadway Classifications
# DAPCZ Area
#
# DONE
# # of Permits in Segment
# Duration of Work Zone
#
# IN PROGRESS
# get_segment_data
# - do this in chunks, maybe 100 at a time?key

import csv
import pdb

import agolutil

from config.config import (
    PERMITS_FILE,
    SEMGENTS_FILE,
    OUTPUT_FILE,
    FIELD_CONFIG,
    GEOM_CONFIG,
)

from config.secrets import AGOL_CREDENTIALS


def score_permits_by_road_class(permits, source_key, score_key):
    # TODO: get road class mapping
    for permit_id in permits.keys():
        max_road_class = permits[permit_id].get("max_road_class")

        print("DO SCORE LOGIC HERE")
        # Critical = 10, Arterial = 7, Collector = 5, Residential = 3

    return permits


def get_max_road_class(permits, road_class_segments):
    for permit_id in permits.keys():
        segments = permits[permit_id].get("segments")

        if segments:

            road_classes = []

            for segment_id in segments:

                segment_id = int(segment_id)

                if segment_id in road_class_segments:
                    road_classes.append(road_class_segments[segment_id]["ROAD_CLASS"])

            if road_classes:
                permits[permit_id]["max_road_class"] = max(road_classes)

            else:
                permits[permit_id]["max_road_class"] = 0

    return permits


def get_segment_data(segment_ids, auth):
    print("get segment data")
    # ready id string as a sql-like statement
    where_ids = ", ".join(f"'{x}'" for x in segment_ids)

    where = "{} in ({})".format(GEOM_CONFIG["primary_key"], where_ids)

    geometry_layer = agolutil.get_item(
        auth=auth,
        service_id=GEOM_CONFIG["service_id"],
        layer_id=GEOM_CONFIG["layer_id"],
    )

    features = geometry_layer.query(
        where=where, outFields=GEOM_CONFIG["outfields"], returnGeometry=False
    )

    return [feature.attributes for feature in features]


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
    duration_key=FIELD_CONFIG["duration"]["source_key"],
    score_key=FIELD_CONFIG["duration"]["score_key"],
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
        # TODO: probably want to handle a KeyError here
        primary[record_id][append_key] = append_dict[record_id][append_key]

    return primary


def score_permits_by_segment_count(
    permits, count_key="segment_count", score_key=FIELD_CONFIG["segments"]["score_key"]
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
            permit_segments[permit_id]["segments"] = []

        permit_segments[permit_id]["segment_count"] += 1
        permit_segments[permit_id]["segments"].append(seg.get("PROPERTYID"))

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
        permits, permits_weighted_with_seg_count, FIELD_CONFIG["segments"]["score_key"]
    )

    # join segment id list to permits
    permits = append_key(permits, permits_with_segments, "segments")

    # **duration scoring**
    permits = score_permits_by_duration(permits)

    # **segment road class scoring**

    segment_ids = [
        segment[FIELD_CONFIG["segments"]["segment_id_key"]] for segment in segments
    ]

    # remove dupes
    segment_ids = list(set(segment_ids))

    # query segment data from ArcGIS Online in chunks
    chunksize = 2500

    segment_road_class = []

    for i in range(0, len(segment_ids), chunksize):
        chunk_of_data = get_segment_data(
            segment_ids[i : i + chunksize], AGOL_CREDENTIALS
        )
        segment_road_class += chunk_of_data

    segment_road_class = index_by_key(segment_road_class, GEOM_CONFIG["primary_key"])

    permits = get_max_road_class(permits, segment_road_class)

    permits = score_permits_by_road_class(
        permits,
        FIELD_CONFIG["road_classes"]["source_key"],
        FIELD_CONFIG["road_classes"]["score_key"],
    )

    # **total up the score
    score_keys = get_all_score_keys(FIELD_CONFIG)

    # todo: total up the score from the score keys

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
