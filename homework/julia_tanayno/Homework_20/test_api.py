import requests
import pytest


@pytest.fixture(scope='session')
def start_end_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def before_after_test():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def new_object():
    body = {
        "data": {
            "color": "red", "size": "medium"
        },
        "name": "My_object"
    }

    headers = {"Content-type": "application/json"}
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body,
        headers=headers
    )

    object_id = response.json()['id']
    yield object_id
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")


def clear(object_id):
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")


def test_get_all_objects(start_end_testing, before_after_test):
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    assert len(response) != 0


@pytest.mark.critical
def test_get_one_object(new_object, before_after_test):
    response = requests.get(f"http://objapi.course.qa-practice.com/object/{new_object}").json()
    assert response['id'] == new_object


@pytest.mark.parametrize(
    'body',
    [
        {
            "data": {"color": "red", "size": "small"},
            "name": "My_object"
        },
        {
            "data": {"color": "green", "size": "medium"},
            "name": "My_object_2"
        },
        {
            "data": {"color": "blue", "size": "large"},
            "name": "My_object_3"
        }
    ]
)
def test_post_object(body, before_after_test):
    headers = {'Content-type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['name'] == body['name']
    assert response_body["data"]["color"] == body["data"]["color"]
    assert response_body["data"]["size"] == body["data"]["size"]

    object_id = response_body["id"]
    clear(object_id)


def test_put_object(new_object, before_after_test):
    body = {"data": {"color": "red", "size": "medium"}, "name": "My_object_UPD"}
    headers = {'Content-type': 'application/json'}
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{new_object}",
        json=body,
        headers=headers
    )
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["name"] == "My_object_UPD", "Name is incorrect"
    assert response.json()["data"]["color"] == "red", "Color is incorrect"


@pytest.mark.medium
def test_patch_object(new_object, before_after_test):
    body = {"data": {"color": "red"}, "name": "My_object_UPD"}
    headers = {"Content-type": "application/json"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{new_object}",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["name"] == "My_object_UPD", "Name is incorrect"
    assert response.json()["data"]["color"] == "red", "Color is incorrect"


def test_delete_object(new_object, before_after_test):
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{new_object}")
    assert response.text == f"Object with id {new_object} successfully deleted"
    assert response.status_code == 200, 'Status code is incorrect'
