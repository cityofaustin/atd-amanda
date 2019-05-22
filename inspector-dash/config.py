PERMITS_FILE = "data/permits.csv"

SEMGENTS_FILE = "data/segments.csv"

OUTPUT_FILE = "permits_scored.csv"

CONFIG = {
    "duration_scoring": {"source_key": "TOTAL_DAYS", "score_key": "duration_score"},
    "segment_scoring": {"source_key": "segment_count", "score_key": "segment_score"},
}