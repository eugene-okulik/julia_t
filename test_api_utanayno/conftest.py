import requests
import pytest

from test_api_utanayno.endpoints.get_object import GetObject
from test_api_utanayno.endpoints.create_object import PostObject
from test_api_utanayno.endpoints.update_object import UpdateObject
from test_api_utanayno.endpoints.delete_object import DeleteObject


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def create_object_endpoint():
    return PostObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


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


def clear(object_id):
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")


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
    clear(object_id)
