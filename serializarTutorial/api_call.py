import requests
import json

data = {"roll_no": 2, "name": "abc", "city": "basu"}
json_data = json.dumps(data)
req = requests.post("http://127.0.0.1:8000/student/new/", data=json_data)

print(req.json())
