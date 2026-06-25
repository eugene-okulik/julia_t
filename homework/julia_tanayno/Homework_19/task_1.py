import requests


def all_objects():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    assert len(response) != 0, 'list is empty'


def one_object():
    object_id = new_object()
    response = requests.get(f"http://objapi.course.qa-practice.com/object/{object_id}").json()
    assert response['id'] == object_id
    clear(object_id)


def post_object():
    body = {
        "data": {
            "color": "red",
            "size": "small"
        },
        "name": "My_object"
    }

    headers = {'Content-type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'
    assert response.json()['name'] == 'My_object', 'Name is incorrect'
    assert response.json()["data"]["color"] == "red", "Color is incorrect"


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

    return response.json()['id']


def clear(object_id):
    requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")


def put_object():
    object_id = new_object()
    body = {"data": {"color": "red", "size": "medium"}, "name": "My_object_UPD"}
    headers = {'Content-type': 'application/json'}
    response = requests.put(
        f"http://objapi.course.qa-practice.com/object/{object_id}",
        json=body,
        headers=headers
    )
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["name"] == "My_object_UPD", "Name is incorrect"
    assert response.json()["data"]["color"] == "red", "Color is incorrect"
    clear(object_id)


def patch_object():
    object_id = new_object()
    body = {"data": {"color": "red"}, "name": "My_object_UPD"}
    headers = {"Content-type": "application/json"}
    response = requests.patch(
        f"http://objapi.course.qa-practice.com/object/{object_id}",
        json=body,
        headers=headers,
    )
    assert response.status_code == 200, "Status code is incorrect"
    assert response.json()["name"] == "My_object_UPD", "Name is incorrect"
    assert response.json()["data"]["color"] == "red", "Color is incorrect"
    clear(object_id)


def delete_object():
    object_id = new_object()
    response = requests.delete(f"http://objapi.course.qa-practice.com/object/{object_id}")
    assert response.text == f"Object with id {object_id} successfully deleted"
    assert response.status_code == 200, 'Status code is incorrect'
