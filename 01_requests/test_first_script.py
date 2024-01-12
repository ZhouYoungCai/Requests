#coding:utf-8

import requests

class Test_Demo:
    def test_demo(self):
        r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        print(r.text)
        print(r.json())