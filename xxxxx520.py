import requests
import json
import base64
# index
r = requests.get('https://www.xxxxx520.org/')
print(r.cookies)
cookies = {}
cookies |= r.cookies.get_dict()
print('cookies  ', cookies)

# login
r = requests.post('https://www.xxxxx520.org/wp-admin/admin-ajax.php', cookies=cookies,
                  data=json.loads(base64.b64decode(b'eyJhY3Rpb24iOiAidXNlcl9sb2dpbiIsICJ1c2VybmFtZSI6ICJvdXRtYW4iLCAicGFzc3dvcmQiOiAiMTIzMTIzMTIzIn0=').decode('utf-8')))
print(r.cookies.get_dict())
cookies |= r.cookies.get_dict()
print('cookies  ', cookies)

# checkout
r = requests.post('https://www.xxxxx520.org/wp-admin/admin-ajax.php', cookies=cookies,
                  data={'action': 'user_qiandao'})
print(r.json())
