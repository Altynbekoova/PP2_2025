import json

with open ("sample-date.json") as file:
    data = json.load(file)

interfaces = data["imdata"]  


print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU'}")
print("-" * 80)


for item in interfaces:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "")
    description = attributes.get("descr", "")  
    speed = attributes.get("speed", "inherit")  
    mtu = attributes.get("mtu", "")

    print(f"{dn:<50} {description:<20} {speed:<7} {mtu}")