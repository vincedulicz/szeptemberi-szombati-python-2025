import requests
from abc import ABC, abstractmethod


class RequestHandler:
    BASE = "https://httpbin.org"

    def get(self, endpoint, params=None, headers=None, timeout=None, allow_redirects=True, auth=None):
        return requests.get(f'{self.BASE}{endpoint}',
                            params=params,
                            headers=headers,
                            timeout=timeout,
                            allow_redirects=allow_redirects,
                            auth=auth)

    def post(self, endpoint, json=None):
        return requests.post(f'{self.BASE}{endpoint}', json=json)


class EndpointTask(ABC):
    def __init__(self, handler: RequestHandler):
        self.handler = handler

    @abstractmethod
    def run(self):
        pass


class Task1(EndpointTask):
    def run(self):
        r = self.handler.get("/get")
        print("1. /get", r.json())


class Task2(EndpointTask):
    def run(self):
        r = self.handler.get("/get", params={"name": "Student", "course": "Python"})
        print("2. params", r.json()["args"])


class Task3(EndpointTask):
    def run(self):
        data = {"title": "Hello", "message": "World"}
        r = self.handler.post("/post", json=data)
        print("3. post", r.json()["json"])


class Task4(EndpointTask):
    def run(self):
        headers = {
            "Authoriziation": "Bearer token123",
            "Custom-Header": "myvalue"
        }
        r = self.handler.get("/headers", headers=headers)
        print("4 fejlécek", r.json()["headers"])


class Task5(EndpointTask):
    def run(self):
        r = self.handler.get("/ip")
        print("5. ip cím") # r.json()["origin"])


class Task6(EndpointTask):
    def run(self):
        try:
            r = self.handler.get("/delay/3", timeout=2)
        except requests.exceptions.Timeout:
            print("6. timeout ok (3 sec) 2 sec limit")
        else:
            print("6. válasz: ", r.json())


class Task7(EndpointTask):
    def run(self):
        r = self.handler.get("/redirect/2", allow_redirects=True)
        print("7. végső url: ", r.url)


class Task8(EndpointTask):
    def run(self):
        r = self.handler.get("/basic-auth/user/pass", auth=("user", "pass"))
        print("8. auth success: ", r.status_code == 200)


class Task9(EndpointTask):
    def run(self):
        for code in [200, 404, 500]:
            r = self.handler.get(f'/status/{code}')
            msg = {200: "OK", 404: "Not found", 500: "server error"}[code]
            print(f'9. status {code} : {msg}')


class Task10(EndpointTask):
    def run(self):
        s = requests.Session()
        s.get(f'{RequestHandler.BASE}/cookies/set?cookie_name=cookie_value')
        r = s.get(f"{RequestHandler.BASE}/cookies")
        print("10. cookie:", r.json()["cookies"])


class TaskRunner:
    def __init__(self):
        h = RequestHandler()
        self.tasks = [
            Task1(h), Task2(h), Task3(h), Task4(h), Task5(h),
            Task6(h), Task7(h), Task8(h), Task9(h), Task10(h)
        ]

    def run_all(self):
        for t in self.tasks:
            t.run()
            print("---\n")


def main():
    TaskRunner().run_all()


main()
