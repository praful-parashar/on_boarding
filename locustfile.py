import json
from locust import HttpLocust, TaskSet, task

class UserAction(TaskSet):

    @task(1)
    def create_merchants(self):
        # header = self.get_header()
        response = self.client.get('/plan/merchants/')

    @task(2)
    def test(self):
        self.client.get('/plan/items/')
        payload = {
            
        }  

    @task(3)

    @task(4)
    def txs(self):
        payload = {
            'store': 1,
            'merchant': 1,
            'items':[1, 2, 3]
        }
        self.client.post('/plan/transactions/', payload)     


class ApplicationUser(HttpLocust):
    task_set = UserAction
    min_wait = 0
    max_wait = 0        