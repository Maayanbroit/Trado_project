from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def index_page(self):
        self.client.get("/")

    @task
    def about_page(self):
        self.client.get("/about")

