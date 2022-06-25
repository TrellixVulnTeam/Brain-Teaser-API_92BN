import json

with open("data.json",encoding="utf8") as file:
    JSON = json.load(file)
    
#alter the data so that each list have a value denoting its index
for i in range(len(JSON)):
    JSON[i]["index"] = i
    
with open("data.json", "w", encoding="utf8") as file:
    json.dump(JSON, file, indent=4)