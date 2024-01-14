import json

from locust import HttpUser, task, between
import random


class BoardServer(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.client.post("/users/sign-in", json={"userId": "ricky",
                                                 "password": "123"})

    @task(3)
    def view_item(self):
        sortStatus = random.choice(["CATEGORIES", "NEWEST", "OLDEST", "HIGHPRICE", "LOWPRICE", "GRADE"])
        categoryId = random.randint(1, 10)
        name = f"테스트 게시글{random.randint(1, 100000)}"
        headers = {'Content-Type': 'application/json'}
        data = {"sortStatus": sortStatus,
                "categoryId": categoryId,
                "name": name}
        # print(data)
        self.client.post("/search", json=data, headers=headers)

# locust -f .\book-server\BookServer.py
