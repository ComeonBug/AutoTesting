import requests



class TestAPI:
    def test_jenkins_api(self):
        url = "http://127.0.0.1:8099/job/iselenium/api/json"
        re = requests.get(url)
        print(re)