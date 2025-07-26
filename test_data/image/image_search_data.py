limit_cases = [
    {
        "case_id": "TC01",
        "desc": "limit=1 with a valid API key should return 1 result",
        "params": {"limit": 1, "api_key": "live_JRURJfM2VsjiOTgpT6Wvs8yX7F29QQq9OFhAPWcdbVCKvKpFWnRpVdTglZZzQXHu"},
        "expected_count": 1
    },
    {
        "case_id": "TC02",
        "desc": "limit=11 with a valid API key should return 11 results",
        "params": {"limit": 11, "api_key": "live_JRURJfM2VsjiOTgpT6Wvs8yX7F29QQq9OFhAPWcdbVCKvKpFWnRpVdTglZZzQXHu"},
        "expected_count": 11
    },
]

mime_type_cases = [
    {
        "case_id": "TC03",
        "desc": "mime_types=png with a valid API key, only PNG and JPG returned",
        "params": {"mime_types": "png", "api_key": "live_JRURJfM2VsjiOTgpT6Wvs8yX7F29QQq9OFhAPWcdbVCKvKpFWnRpVdTglZZzQXHu"},
        "expected_suffix": [".png", ".jpg"]
    },
    {
        "case_id": "TC04",
        "desc": "mime_types=png,gif with a valid API key, only PNG, JPG, and GIF returned",
        "params": {"mime_types": "png,gif", "api_key": "live_JRURJfM2VsjiOTgpT6Wvs8yX7F29QQq9OFhAPWcdbVCKvKpFWnRpVdTglZZzQXHu"},
        "expected_suffix": [".png", ".jpg", ".gif"]
    },
]

has_breeds_cases = [
    {
        "case_id": "TC05",
        "desc": "has_breeds=true with a valid API key, only images with breed info returned",
        "params": {"has_breeds": True, "api_key": "live_JRURJfM2VsjiOTgpT6Wvs8yX7F29QQq9OFhAPWcdbVCKvKpFWnRpVdTglZZzQXHu"}
    }
]

include_breeds_cases = [
    {
        "case_id": "TC06",
        "desc": "include_breeds=1 with a valid API key, breeds key should be present",
        "params": {"include_breeds": 1, "api_key": "live_JRURJfM2VsjiOTgpT6Wvs8yX7F29QQq9OFhAPWcdbVCKvKpFWnRpVdTglZZzQXHu"}
    },
    {
        "case_id": "TC07",
        "desc": "include_breeds=0 with a valid API key, breeds key should be missing",
        "params": {"include_breeds": 0, "api_key": "live_JRURJfM2VsjiOTgpT6Wvs8yX7F29QQq9OFhAPWcdbVCKvKpFWnRpVdTglZZzQXHu"}
    },
]

empty_or_invalid_api_key_cases = [
    {
        "case_id": "TC08",
        "desc": "Invalid API key provided, should return 10 results with no breed info, no categories",
        "params": {"api_key": "Invalid-api-key"}
    },
    {
        "case_id": "TC09",
        "desc": "No API key provided,should return 10 results with no breed info, no categories",
        "params": {"api_key": None}
    },
    {
        "case_id": "TC10",
        "desc": "has_breeds with no API key, should return 10 results with no breed info",
        "params": {"has_breeds": True}
    },
    {
        "case_id": "TC11",
        "desc": "include_categories with no API key, should return 10 results with no breed info, no categories",
        "params": {"include_categories": 1}
    },
    {
        "case_id": "TC12",
        "desc": "limit=11 with no API key, should return 10 results with no breed info, no categories",
        "params": {"limit": 11}
    },
]

image_url_cases = [
    {
        "case_id": "TC13",
        "desc": "should return results with live image urls",
        "params": {"api_key": "live_JRURJfM2VsjiOTgpT6Wvs8yX7F29QQq9OFhAPWcdbVCKvKpFWnRpVdTglZZzQXHu"}
    },
]

# Add more parametrized test data as needed!
