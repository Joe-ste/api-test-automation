import requests
import logging
from urllib.parse import urljoin

class BaseAPI:
    def __init__(self, base_url: str, api_key: str = None, default_timeout: int = 10):
        self.base_url = base_url
        self.session = requests.Session()
        self.default_timeout = default_timeout
        if api_key:
            self.session.headers.update({"x-api-key": api_key})
        self.logger = logging.getLogger(self.__class__.__name__)

    def request(self, method: str, path: str, timeout: int = None, **kwargs) -> requests.Response:
        url = urljoin(self.base_url, path)
        timeout = timeout or self.default_timeout
        self.logger.info(f"Request: {method} {url} | timeout={timeout}")
        try:
            response = self.session.request(method, url, timeout=timeout, **kwargs)
            duration = response.elapsed.total_seconds()
            self.logger.info(
                f"Response: {method} {url} | status={response.status_code} | time={duration:.3f}s"
            )
            if duration > timeout:
                self.logger.warning(
                    f"Slow response (> timeout): {duration:.3f}s for {method} {url}"
                )
            return response
        except requests.Timeout:
            self.logger.error(f"Request to {url} timed out after {timeout}s")
            raise AssertionError(f"Request to {url} timed out after {timeout}s")
        except requests.RequestException as e:
            self.logger.error(f"Request failed: {method} {url} | error: {e}")
            raise AssertionError(f"Request failed: {e}")

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.request("GET", path, **kwargs)
    def post(self, path: str, **kwargs) -> requests.Response:
        return self.request("POST", path, **kwargs)
    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.request("DELETE", path, **kwargs)
    def put(self, path: str, **kwargs) -> requests.Response:
        return self.request("PUT", path, **kwargs)
