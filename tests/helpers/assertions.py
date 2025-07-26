from jsonschema import validate
import requests

def assert_url_live(url, timeout=5):
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        assert response.status_code == 200, f"URL not live: {url} (status {response.status_code})"
    except Exception as e:
        raise AssertionError(f"URL check failed for {url}: {e}")

def assert_all_urls_live(results, timeout=5):
    errors = []
    for item in results:
        url = item.get("url")
        if not url:
            errors.append(f"Missing url in item: {item}")
            continue
        try:
            assert_url_live(url, timeout=timeout)
        except AssertionError as e:
            errors.append(str(e))
    assert not errors, "Some image URLs are not live:\n" + "\n".join(errors)

def assert_status_and_schema(response, json_schema, expected_status=200):
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
    validate(response.json(), json_schema)

def assert_all_have_suffix(results, suffixies):
    for item in results:
        assert item["url"].endswith(tuple(suffixies)), f"URL does not end with {suffixies}: {item['url']}"

def assert_all_have_breeds(results):
    for item in results:
        assert len(item.get("breeds")) > 0, f"Expected breeds info in {item}"

def assert_all_have_key(results, key):
    for item in results:
        assert key in item, f"Expected key '{key}' in result: {item}"

def assert_all_missing_or_empty(results, key):
    for item in results:
        assert key not in item or not item[key], f"Expected key '{key}' missing or empty: {item}"

def assert_empty_response(results):
    assert results == [] or len(results) == 0

def assert_results_count(results, expected_count):
    assert len(results) == expected_count, f"Expected {expected_count} results, got {len(results)}"

def assert_max_count(results, max_count):
    assert len(results) <= max_count, f"Expected <= {max_count} results, got {len(results)}"

def assert_keys_in_results(results, keys):
    for item in results:
        for key in keys:
            assert key in item, f"Missing key '{key}' in: {item}"
