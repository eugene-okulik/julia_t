import requests
import allure

from test_api_utanayno.endpoints.endpoint import Endpoint


class UpdateObject(Endpoint):
    @allure.step("Update object (put, update the whole object)")
    def update_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f"{self.url}/{object_id}", json=body, headers=headers
        )
        self.json = self.response.json()
        return self.response


    @allure.step("Update object (patch, update the object partially)")
    def patch_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f"{self.url}/{object_id}", json=body, headers=headers
        )
        self.json = self.response.json()
        return self.response
