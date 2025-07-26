from .base_api import BaseAPI

class ImagesAPI(BaseAPI):
    
    def search(self, params=None, headers=None, timeout=None):
        return self.get("images/search", params=params, headers=headers, timeout=timeout)