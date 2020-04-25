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