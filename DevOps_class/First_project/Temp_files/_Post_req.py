import datetime
from flask import jsonify

import requests
res = requests.post('http://127.0.0.1:5000/data/5', json={
    'user_id': 55553,
    'user_name': 'shaked',
    'creation_date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
})

if res.ok:
    print(res.json())
else:
    print(res.json())


