import requests

# requests1 = requests.put('https://httpbin.org/put', data={'key': 'value'})
# requests1 = requests.delete('https://httpbin.org/delete')
# requests1 = requests.head('https://httpbin.org/get')
# requests1 = requests.options('https://httpbin.org/get')

class Test_Demo:
    def test_get(self):
        r = requests.get("http://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200