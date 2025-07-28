from typing import Any, List, Dict, Sequence
from jsonschema import validate
import requests

def assert_url_live(url: str, timeout: int = 5) -> None:
    """Assert that the given URL is reachable (status 200) via HEAD request."""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        assert response.status_code == 200, f"URL not live: {url} (status {response.status_code})"
    except Exception as e:
        raise AssertionError(f"URL check failed for {url}: {e}")

def assert_all_urls_live(results: List[Dict[str, Any]], timeout: int = 5) -> None:
    """Assert that all 'url' fields in the list of dicts are live."""
    errors: List[str] = []
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

def assert_status_and_schema(response: requests.Response, json_schema: dict, expected_status: int = 200) -> None:
    """Assert response status and that the JSON matches the schema."""
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
    validate(response.json(), json_schema)

def assert_all_have_suffix(results: List[Dict[str, Any]], suffixes: Sequence[str]) -> None:
    """Assert all URLs in the list end with one of the given suffixes."""
    for item in results:
        assert item["url"].endswith(tuple(suffixes)), f"URL does not end with {suffixes}: {item['url']}"

def assert_all_have_breeds(results: List[Dict[str, Any]]) -> None:
    """Assert all items have a non-empty 'breeds' list."""
    for item in results:
        assert len(item.get("breeds", [])) > 0, f"Expected breeds info in {item}"

def assert_all_have_key(results: List[Dict[str, Any]], key: str) -> None:
    """Assert all items have the given key."""
    for item in results:
        assert key in item, f"Expected key '{key}' in result: {item}"

def assert_all_missing_or_empty(results: List[Dict[str, Any]], key: str) -> None:
    """Assert key is missing or empty in all results."""
    for item in results:
        assert key not in item or not item[key], f"Expected key '{key}' missing or empty: {item}"

def assert_empty_response(results: Any) -> None:
    """Assert results are empty (list or len==0)."""
    assert results == [] or len(results) == 0, f"Expected empty response, got: {results}"

def assert_results_count(results: List[Any], expected_count: int) -> None:
    """Assert results contain exactly expected_count items."""
    assert len(results) == expected_count, f"Expected {expected_count} results, got {len(results)}"

def assert_max_count(results: List[Any], max_count: int) -> None:
    """Assert results contain at most max_count items."""
    assert len(results) <= max_count, f"Expected <= {max_count} results, got {len(results)}"

def assert_keys_in_results(results: List[Dict[str, Any]], keys: Sequence[str]) -> None:
    """Assert all specified keys exist in every item of results."""
    for item in results:
        for key in keys:
            assert key in item, f"Missing key '{key}' in: {item}"
