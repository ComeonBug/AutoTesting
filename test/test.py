import requests

class TestApi:
    def test_api(self):
        re = requests.get('https://httpbin.org/get')
        assert re.status_code == 300