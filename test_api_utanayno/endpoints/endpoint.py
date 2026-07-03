import allure
import requests


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    response = None
    json = None
    headers = {"Content-type": "application/json"}

    @allure.step('Delete object')
    def delete_object(self, object_id=None):
        object_id = object_id or self.json.get("id")
        requests.delete(f"{self.url}/{object_id}")

    @allure.step('Check that response is 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200, '200 is not 200'

    @allure.step("Check object's id")
    def check_object_id(self, object_id):
        assert self.json['id'] == object_id

    @allure.step('Check that object name is as sent')
    def check_object_name_is_correct(self, name):
        assert self.json["name"] == name, 'name is not as sent'

    @allure.step("Check that object color is as sent")
    def check_object_color_is_correct(self, color):
        assert self.json["data"]["color"] == color, "color is not as sent"

    @allure.step("Check that object size is as sent")
    def check_object_size_is_correct(self, size):
        assert self.json["data"]["size"] == size, "size is not as sent"

    @allure.step("Check that object is not found")
    def check_object_not_found(self):
        assert self.response.status_code == 404
