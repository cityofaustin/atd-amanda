# TODO
# Roadway Classifications
# DAPCZ Area
# Duration of Work Zone
# 
# DONE
# # of Permits in Segment

import csv
import pdb

PERMITS_FILE = "data/permits.csv"

SEMGENTS_FILE = "data/segments.csv"

def score_permits_by_duration(permits, duration_key="TOTAL_DAYS", score_key="duration_score")

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


def score_permits_by_segment_count(permits, count_key="segment_count", score_key="segment_score"):
    
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

    permits_with_seg_count = segments_per_permit(segments)

    permits_weighted_with_seg_count = weight_permits_by_segment_count(permits_with_seg_count)

    # join segment weight to permits
    permits = append_key(permits, permits_weighted_with_seg_count, "segment_count_weighted")
    pdb.set_trace()

results = main()

# sort the dicts by seg vals
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# results = sorted(results.items(), key=lambda kv: kv[1], reverse=True)


pdb.set_trace()

