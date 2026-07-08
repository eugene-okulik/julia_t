import pytest
import allure

TEST_DATA = [
    {"data": {"color": "red", "size": "small"}, "name": "My_object"},
    {"data": {"color": "green", "size": "medium"}, "name": "My_object_2"},
    {"data": {"color": "blue", "size": "large"}, "name": "My_object_3"},
]


@allure.feature("Objects")
@allure.story("Get objects")
@allure.title("Получение всех объектов")
def test_get_all_objects(get_object_endpoint, before_after_test, start_end_testing):
    get_object_endpoint.get_all_posts()
    get_object_endpoint.check_status_is_200()


@allure.feature("Objects")
@allure.story("Get objects")
@allure.title("Получение одного объекта")
@pytest.mark.critical
def test_get_one_object(get_object_endpoint, new_object, before_after_test):
    get_object_endpoint.get_object_by_id(new_object)
    get_object_endpoint.check_status_is_200()
    get_object_endpoint.check_object_id(new_object)


@allure.feature("Objects")
@allure.story("Post objects")
@allure.title("Добавление объекта")
@pytest.mark.parametrize("data", TEST_DATA)
def test_post_object(create_object_endpoint, delete_object_endpoint, data, before_after_test):
    create_object_endpoint.create_new_object(body=data)
    create_object_endpoint.check_status_is_200()
    create_object_endpoint.check_object_name_is_correct(data["name"])
    create_object_endpoint.check_object_color_is_correct(data["data"]["color"])
    create_object_endpoint.check_object_size_is_correct(data["data"]["size"])
    delete_object_endpoint.delete_object(create_object_endpoint.json['id'])


@allure.feature("Objects")
@allure.story("Update objects")
@allure.title("Изменение объекта целиком")
def test_put_object(new_object, update_object_endpoint, before_after_test):
    body = {"data": {"color": "red_UPD", "size": "medium_UPD"}, "name": "My_object_UPD"}
    update_object_endpoint.update_object(new_object, body)
    update_object_endpoint.check_status_is_200()
    update_object_endpoint.check_object_name_is_correct(body["name"])
    update_object_endpoint.check_object_color_is_correct(body["data"]["color"])
    update_object_endpoint.check_object_size_is_correct(body["data"]["size"])


@allure.feature("Objects")
@allure.story("Update objects")
@allure.title("Изменение объекта частично")
@pytest.mark.medium
def test_patch_object(new_object, update_object_endpoint, before_after_test):
    body = {"data": {"color": "red"}, "name": "My_object_UPD"}
    update_object_endpoint.patch_object(new_object, body)
    update_object_endpoint.check_status_is_200()
    update_object_endpoint.check_object_name_is_correct(body["name"])
    update_object_endpoint.check_object_color_is_correct(body["data"]["color"])


@allure.feature("Objects")
@allure.story("Delete objects")
@allure.title("Удаление объекта")
def test_delete_object(new_object, delete_object_endpoint, before_after_test):
    delete_object_endpoint.delete_object(new_object)
    delete_object_endpoint.check_status_is_200()
    delete_object_endpoint.check_sent_object_is_deleted(new_object)
    delete_object_endpoint.delete_object(new_object)
    delete_object_endpoint.check_object_not_found()
