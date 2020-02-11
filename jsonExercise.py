import json

data = """
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]"""

info = json.loads(data)
print("User Count ::", len(info))

for item in info:
    print("Name: ", item["name"])
    print("id: ", item["id"])
    print("x: ", item["x"])

## Examples from RealPython Serializing JSON

data_realstring = {"president": {"name": "Narendra Modi", "species": "Homo Sapiens"}}
with open("data_file.json", "w") as write_file:
    json.dump(data_realstring, write_file, indent=4)

json_string = json.dumps(data_realstring, indent=4)

print("JSON Object ::", json_string)

