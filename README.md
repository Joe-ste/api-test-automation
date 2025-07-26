# TheCatAPI Automated API Test Suite

## Overview

This repository contains an automated API test suite for [TheCatAPI](https://thecatapi.com/) `/images/search` endpoint, implemented in **Python** using **pytest**.  
It is modular, parametrized, and designed to be easily extended. The suite covers both positive and negative scenarios to ensure robustness and contract compliance.

---

## Test Case Table

| Case ID | Description                                                     | Input Params                 | Steps                                                                                                                                           | Expected Result / Validation                  |
|---------|-----------------------------------------------------------------|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| TC01    | limit=1 with a valid API key should return 1 result             | `limit=1, api_key=VALID`     | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check results count.                                                    | 1. Response status is 200.<br>2. 1 result returned.               |
| TC02    | limit=11 with a valid API key should return 11 results          | `limit=11, api_key=VALID`    | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check results count.                                                    | 1. Response status is 200.<br>2. 11 results returned.             |
| TC03    | mime_types=png, only PNG and JPG returned (API quirk)           | `mime_types=png, api_key=VALID` | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check all URLs end with `.png` or `.jpg`.                             | 1. Response status is 200.<br>2. All URLs end with `.png` or `.jpg`.            |
| TC04    | mime_types=png,gif, only PNG, JPG, GIF returned                 | `mime_types=png,gif, api_key=VALID` | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check all URLs end with `.png`, `.jpg`, or `.gif`.                  | 1. Response status is 200.<br>2. All URLs end with `.png`, `.jpg`, or `.gif`.   |
| TC05    | has_breeds=true, only images with breed info returned           | `has_breeds=true, api_key=VALID` | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check each result contains non-empty `breeds`.                      | 1. Response status is 200.<br>2. All results have non-empty `breeds`.           |
| TC06    | include_breeds=1, breeds key should be present                  | `include_breeds=1, api_key=VALID` | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check all results contain `breeds` key.                             | 1. Response status is 200.<br>2. All results have `breeds` key.                 |
| TC07    | include_breeds=0, breeds key should be missing                  | `include_breeds=0, api_key=VALID` | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check `breeds` key missing or empty in results.                     | 1. Response status is 200.<br>2. All results missing or have empty `breeds`.    |
| TC08    | Invalid API key, should return 10 results, no breed/category    | `api_key=INVALID`            | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check count, no `breeds`, no `categories`.                         | 1. Response status is 200.<br>2. ≤10 results.<br>3. No `breeds` or `categories`. |
| TC09    | No API key, should return 10 results, no breed/category         | (no key)                     | 1. Send GET `/images/search`.<br>2. Validate response.<br>3. Check count, no `breeds`, no `categories`.                                       | 1. Response status is 200.<br>2. ≤10 results.<br>3. No `breeds` or `categories`. |
| TC10    | has_breeds with no API key, 10 results, no breed info           | `has_breeds=true`            | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check count, no `breeds`.                                            | 1. Response status is 200.<br>2. ≤10 results.<br>3. No `breeds`.                |
| TC11    | include_categories with no API key, 10 results, no breed/category | `include_categories=1`      | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check count, no `breeds`, no `categories`.                         | 1. Response status is 200.<br>2. ≤10 results.<br>3. No `breeds` or `categories`. |
| TC12    | limit=11 with no API key, 10 results, no breed/category         | `limit=11`                   | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. Check count, no `breeds`, no `categories`.                         | 1. Response status is 200.<br>2. ≤10 results.<br>3. No `breeds` or `categories`. |
| TC13    | should return results with live image urls                      | `api_key=VALID`              | 1. Send GET `/images/search` with params.<br>2. Validate response.<br>3. For each result, GET the image URL and check HTTP 200.             | 1. Response status is 200.<br>2. All URLs are live and return HTTP 200.         |


---

## Validation Approach

- **Status and Schema Validation**:  
  Each test checks for HTTP 200 and validates the response using strict JSON schema definitions (with [`jsonschema`](https://python-jsonschema.readthedocs.io/)).
- **Field and Content Checks**:  
  Tests validate counts, the presence/absence of fields (`breeds`, `categories`), content correctness (URL suffix), and live image access.
- **Negative Scenarios**:  
  Includes cases with missing or invalid API keys, and checks API default/fallback behaviors.
- **Live URL Validation**:  
  Ensures that all returned image URLs are actually accessible (HTTP 200).

---

## Why This Type of Validation?

- **Schema validation** catches breaking changes in the API response format.
- **Content and field checks** ensure real business/user requirements are met, and filter logic works.
- **Negative scenarios** ensure api key works.
- **Live URL checks** help verify external resource availability.

---

## How To Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
2. **Run all tests:**
   ```bash
   pytest
   ```
   *(Or specify an environment:)*  
   ```bash
   pytest --env=test
   ```
---

## How To Extend

- Add new scenarios by extending test data files in `test_data/`, giving each a new `case_id` and description.
- Add new JSON schemas to `schema/` if new endpoints or stricter validation are needed.
- Reuse or extend assertion helpers in `tests/helpers/assertions.py` as you grow coverage.

---

## Folder Structure

```text
.
├── api/
│   ├── base_api.py                    # Base API object for inheriting
│   └── image_api.py                   # API object(s)
├── schema/
│   └── image_json_schema.py           # JSON schemas for response validation
├── test_data/
│   ├── image                          
│   └── image_search_data.py           # Test case data (case_id, desc, params) for image search endpoint test
├── tests/
│   ├── conftest.py                    # Fixtures (env, api object, test data)
│   ├── helpers/
│   │   └── assertions.py              # Assertion helper functions
│   └── image/
│       └── test_image_search.py       # All image search endpoint tests
├── requirements.txt
├── README.md
```

---

## Sample Test Implementation

```python
@pytest.mark.parametrize(
    "data",
    image_search_data.limit_cases,
    indirect=True,
    ids=lambda x: x["case_id"]
)
def test_limit_results(self, images_api, data):
    resp = images_api.search(params=data["params"])
    assert_status_and_schema(resp, image_search_response_schema)
    assert_results_count(resp.json(), data["expected_count"])
```

---


