import requests
import allure

from test_api_utanayno.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step("Get all objects")
    def get_all_posts(self):
        self.response = requests.get(self.url)
        self.json = self.response.json()
        return self.response

    @allure.step("Check that there are objects")
    def check_that_there_are_objects(self):
        assert len(self.json) > 0

    @allure.step("Get object by id")
    def get_object_by_id(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        self.json = self.response.json()
