import datetime
from flask import jsonify
import requests
user_id = int(input("enter user id"))
res = requests.get('http://127.0.0.1:5000/data/{}'.format(user_id))
if res.ok:
    print(res.json())
else:
    print(res.json())


