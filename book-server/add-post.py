from locust import HttpUser, task, between
import random


class AddPosts(HttpUser):
    wait_time = between(1, 2)  # 각 스래드 별 1~2초 사이의 랜덤한 시간 간격 으로 여유 시간을 줌

    def on_start(self):
        self.client.post("/users/sign-in", json={"userId": "ricky",
                                                 "password": "123"})

    @task
    def add_post(self):
        self.client.post("/posts", json={
            "name": "테스트 게시글" + str(random.randint(1, 100000)),
            "contents": "테스트 컨텐츠" + str(random.randint(1, 100000)),
            "categoryId": random.randint(1, 10),
            "fileId": random.randint(1, 10),
        })

# locust -f .\book-server\add-post.py
