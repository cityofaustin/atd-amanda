PERMITS_FILE = "data/permits.csv"

SEMGENTS_FILE = "data/segments.csv"

OUTPUT_FILE = "permits_scored.csv"

FIELD_CONFIG = {
    "duration": {"source_key": "TOTAL_DAYS", "score_key": "duration_score"},
    "segments": {"source_key": "segment_count", "score_key": "segment_score", "segment_id_key" : "PROPERTYID"},
    "road_classes" : {"source_key": "max_road_class", "score_key": "road_class_score"}
}

GEOM_CONFIG = {
    "service_id" : "a78db5b7a72640bcbb181dcb88817652",
    "layer_id" : 0,
    "primary_key" : "SEGMENT_ID",
    "outfields" : "ROAD_CLASS, SEGMENT_ID"
}