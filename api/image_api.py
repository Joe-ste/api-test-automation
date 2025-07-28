from typing import Optional, Dict, Any
from .base_api import BaseAPI
import requests

class ImagesAPI(BaseAPI):
    """
    API client for image search endpoints.
    """

    def search(
        self,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None
    ) -> requests.Response:
        """
        Search for images.
        
        Args:
            params: Query parameters for the API call.
            headers: Optional headers to send with the request.
            timeout: Timeout for the request in seconds.

        Returns:
            requests.Response: The HTTP response object.
        """
        return self.get("images/search", params=params, headers=headers, timeout=timeout)
