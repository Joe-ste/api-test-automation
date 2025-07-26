import pytest
from tests.conftest import data
from tests.helpers.assertions import *
from test_data.image import image_search_data
from schema.image_json_shema import image_search_response_schema, image_search_response_no_api_key_schema
class TestImageSearch:

    def test_basic_search(self, images_api):
        resp = images_api.search()
        assert_status_and_schema(resp, image_search_response_schema)

    @pytest.mark.parametrize("data", image_search_data.limit_cases, indirect=True, ids=lambda x: x["case_id"])
    def test_limit_results(self, images_api, data):
        resp = images_api.search(params=data["params"])
        assert_status_and_schema(resp, image_search_response_schema)
        assert_results_count(resp.json(), data["expected_count"])

    @pytest.mark.parametrize("data", image_search_data.mime_type_cases, indirect=True, ids=lambda x: x["case_id"])
    def test_filter_by_mime_types(self, images_api, data):
        resp = images_api.search(params=data["params"])
        assert_status_and_schema(resp, image_search_response_schema)
        assert_all_have_suffix(resp.json(), data["expected_suffix"])

    @pytest.mark.parametrize("data", image_search_data.has_breeds_cases, indirect=True, ids=lambda x: x["case_id"])
    def test_breed_info_only(self, images_api, data):
        resp = images_api.search(params=data["params"])
        assert_all_have_breeds(resp.json())

    @pytest.mark.parametrize("data", image_search_data.include_breeds_cases, indirect=True, ids=lambda x: x["case_id"])
    def test_include_breeds(self, images_api, data):
        resp = images_api.search(params=data["params"])
        assert_status_and_schema(resp, image_search_response_schema)
        if data["params"]["include_breeds"] == 0:
            assert_all_missing_or_empty(resp.json(), "breeds")
        else:
            assert_all_have_key(resp.json(), "breeds")

    @pytest.mark.parametrize("data", image_search_data.empty_or_invalid_api_key_cases, indirect=True, ids=lambda x: x["case_id"])
    def test_empty_or_invalid_api_key(self, images_api, data):
        resp = images_api.search(params=data["params"])
        assert_status_and_schema(resp, image_search_response_no_api_key_schema)
        assert_max_count(resp.json(), 10)

    @pytest.mark.parametrize("data", image_search_data.image_url_cases, indirect=True, ids=lambda x: x["case_id"])
    def test_image_url(self, images_api, data):
        resp = images_api.search(params=data["params"])
        assert_status_and_schema(resp, image_search_response_schema)
        assert_all_urls_live(resp.json())
