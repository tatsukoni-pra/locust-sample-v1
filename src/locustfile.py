from locust import HttpUser, task, constant_pacing

class WEBsiteUser(HttpUser):
    #  1タスク = 1秒間に1回リクエストを送信する
    wait_time = constant_pacing(1)

    @task
    def view_top(self):
        self.client.get("/first")
