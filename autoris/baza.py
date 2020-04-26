import json

def addUser(put,name,password):
    with open(put, "r") as read_file:
        data = json.load(read_file)
    res = True
    for k,v in data["users"].items():
        if k == name:
            res=False
            break
    if res:
        data["users"][name]=[{},password]
    with open(put, "w") as write_file:
        json.dump(data, write_file, indent=4)
    return res

def checkUser(put,name,password):
    with open(put, "r") as read_file:
        data = json.load(read_file)
    res = False
    for k,v in data["users"].items():
        if k == name and v[1] == password:
            res = True
            break
    return res
