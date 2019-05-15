# TODO
# Roadway Classifications
# DAPCZ Area
# 
# DONE
# # of Permits in Segment
# Duration of Work Zone

import csv
import pdb

from config import *


def total_score(permits, score_keys, total_score_key_name="total_score"):
    return permits

def score_permits_by_duration(
        permits,
        duration_key=CONFIG["duration_scoring"]["source_key"],
        score_key=CONFIG["duration_scoring"]["score_key"]
    ):
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
    '''
    primary: dict that will receive the new key
    append_dict: dict that contains the data that will be appended
      to the primary
    append_key: the key/value that will be added to the primary
    '''

    for record_id in append_dict:
        # TODO: probably want to handle a KeyError here
        primary[record_id][append_key] = append_dict[record_id][append_key]

    return primary


def score_permits_by_segment_count(permits, count_key="segment_count", score_key=CONFIG["segment_scoring"]["score_key"]):
    
    for permit_id in permits:
        count = permits[permit_id][count_key]

        if count > 1:
            permits[permit_id][score_key] = 10
        if count <= 1:
            permits[permit_id][score_key] = 5

    return permits


def segments_per_permit(segments):
    # count the number of segments per permit
    # return a dict of permit ID with count of segments
    segments_count = {}

    for seg in segments:
        # FOLDERRSN is the unique permit identifer
        permit_id = seg.get("FOLDERRSN")

        if permit_id not in segments_count:
            segments_count[permit_id] = { "segment_count" :  0 }

        segments_count[permit_id]["segment_count"] += 1

    return segments_count


def index_by_key(list_of_dicts, key):
    # transform a list of dicts into a dict with a top-level index
    return { row[key] : row  for row in list_of_dicts}


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

    # **segment scoring**
    permits_with_seg_count = segments_per_permit(segments)

    permits_weighted_with_seg_count = score_permits_by_segment_count(permits_with_seg_count)

    # join segment weight to permits
    permits = append_key(
        permits,
        permits_weighted_with_seg_count,
        CONFIG["segment_scoring"]["score_key"]
    )

    # **duration scoring**
    permits = score_permits_by_duration(permits)

    pdb.set_trace()

results = main()

# sort the dicts by seg vals
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# results = sorted(results.items(), key=lambda kv: kv[1], reverse=True)


pdb.set_trace()

