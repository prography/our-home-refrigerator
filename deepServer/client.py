import requests
from config.config import get_config

config = get_config()

json = {config.user_id_name : 'X12fS', config.ip_name : '127.0.0.1'}
URL = 'http://192.168.118.1:12345/login'
res = requests.get(URL, json=json)

print(res.text)

