image_no_api_key_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "url": {"type": "string", "format": "uri"},
        "width": {"type": "integer"},
        "height": {"type": "integer"}
    },
    "required": ["id", "url", "width", "height"],
    "additionalProperties": False
}

image_search_response_no_api_key_schema = {
    "type": "array",
    "items": image_no_api_key_schema
}

categories_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
        "required": ["id", "name"],
    }
}

breeds_schema = breed_schema = {
    "type": "object",
    "properties": {
        "weight": {
            "type": "object",
            "properties": {
                "imperial": {"type": "string"},
                "metric": {"type": "string"}
            },
            "required": ["imperial", "metric"]
        },
        "id": {"type": "string"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "origin": {"type": "string"},
        "cfa_url": {"type": "string"},
        "temperament": {"type": "string"},
        "country_codes": {"type": "string"},
        "country_code": {"type": "string"},
        "life_span": {"type": "string"},
        "indoor": {"type": "integer"},
        "lap": {"type": "integer"},
        "alt_names": {"type": "string"},
        "adaptability": {"type": "integer"},
        "affection_level": {"type": "integer"},
        "child_friendly": {"type": "integer"},
        "cat_friendly": {"type": "integer"},
        "dog_friendly": {"type": "integer"},
        "energy_level": {"type": "integer"},
        "grooming": {"type": "integer"},
        "health_issues": {"type": "integer"},
        "intelligence": {"type": "integer"},
        "shedding_level": {"type": "integer"},
        "social_needs": {"type": "integer"},
        "stranger_friendly": {"type": "integer"},
        "vocalisation": {"type": "integer"},
        "bidability": {"type": "integer"},
        "experimental": {"type": "integer"},
        "hairless": {"type": "integer"},
        "natural": {"type": "integer"},
        "rare": {"type": "integer"},
        "rex": {"type": "integer"},
        "suppressed_tail": {"type": "integer"},
        "short_legs": {"type": "integer"},
        "wikipedia_url": {"type": "string"},
        "vetstreet_url": {"type": "string"},
        "vcahospitals_url": {"type": "string"},
        "reference_image_id": {"type": "string"},
        "hypoallergenic": {"type": "integer"},
    },
    "required": ["id", "name", "weight", "description", "origin"],
    "additionalProperties": True
}


image_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "url": {"type": "string", "format": "uri"},
        "width": {"type": "integer"},
        "height": {"type": "integer"},
        "breeds": {
            "type": "array",
            "items": breeds_schema
        },
        "categories": categories_schema
    },
    "required": ["id", "url", "width", "height"]
}

image_search_response_schema = {
    "type": "array",
    "items": image_schema
}

