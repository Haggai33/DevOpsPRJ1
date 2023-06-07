import datetime
from flask import jsonify
import requests

user_id = int(input("enter user id"))
new_user_name = input("enter new user name")

res = requests.put('http://127.0.0.1:5000/data/{}'.format(user_id), json={'user_name': new_user_name})

if res.ok:
    print(res.json())
else:
    print(res.json())




