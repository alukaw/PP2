import json
json_file = 'sample-data.json'

with open(json_file, 'r') as file:
    data = json.dumps(file)