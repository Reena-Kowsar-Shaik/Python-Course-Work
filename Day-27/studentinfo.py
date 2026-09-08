student={
    "name":"reena",
    "age":22,
    "course":"Python"
}
import json
json_data= json.dumps(student)
print(json_data)

student=json.loads(json_data)
print(student)
print(type(student))

'''with open("data.json",'r') as file:
    data= json.load(file)

data["username"]="kowsar"
data["skills"].append("ml")

with open("data.json",'w') as file:
    json.dump(data,file,indent=4)'''