import json
json_file = "sample-data.json"

with open(json_file, 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print("-" * 80)

for item in data["imdata"][:3]:
    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes["dn"]
    descr = attributes["descr"] 
    speed = attributes["speed"] 
    mtu = attributes["mtu"]

    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<10}")