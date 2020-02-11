import json
import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

print(json.dumps(todos[-2:], indent=4))
