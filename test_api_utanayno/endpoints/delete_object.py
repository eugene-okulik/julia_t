import requests
import allure

from test_api_utanayno.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):
    @allure.step("Delete object")
    def delete_object(self, object_id):
        self.response = requests.delete(f"{self.url}/{object_id}")


    @allure.step("Check that sent object is deleted")
    def check_sent_object_is_deleted(self, object_id):
        assert self.response.text == f"Object with id {object_id} successfully deleted"
