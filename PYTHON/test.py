import requests

with requests.Session() as c:
    url = ""
    USERNAME = ''
    PASSWORD = ''
    c.get(url)
    login_data = {"username":USERNAME,'password':PASSWORD}
    r=c.post(url,data=login_data)
    print(r)