import datetime
from flask import jsonify
import requests


user_id = int(input("Enter user id"))
res = requests.delete(f'http://127.0.0.1:5000/data/{user_id}')

if res.ok:
    print(res.json())
else:
    print(res.json())


#
# x = range(1, 10000)
#1

# for y in x:
#     res = requests.delete(f'http://127.0.0.1:5000/data/{y}')