from locust import task, HttpUser
import random


class MemeUser(HttpUser):
    @task(1)
    def get_all_objects(self):
        self.client.get("/object")

    @task(2)
    def get_one_object(self):
        self.client.get(f'/object/{random.choice(range(1, 11))}')

    @task(3)
    def post_object(self):
        self.client.post('/object', json={
                              "data": {"color": "white","size": "big"},
                              "name": "Locust_object"
                                }
                         )

    @task(3)
    def delete_object(self):
        self.client.delete(f'/object/{random.choice(range(20, 1457))}')
