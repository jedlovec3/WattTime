import requests
from requests.auth import HTTPBasicAuth
login_url = 'https://api2.watttime.org/v2/login'
rsp = requests.get(login_url, auth=HTTPBasicAuth('jedlovec3', '4ojf*^5T35onHN'))
print(rsp.json())


login_url = 'https://api2.watttime.org/v2/login'
token = requests.get(login_url, auth=HTTPBasicAuth('jedlovec3', '4ojf*^5T35onHN')).json()['token']

list_url = 'https://api2.watttime.org/v2/ba-access'
headers = {'Authorization': 'Bearer {}'.format(token)}
params = {'all': 'false'}
rsp = requests.get(list_url, headers=headers, params=params)
print(rsp.text)
