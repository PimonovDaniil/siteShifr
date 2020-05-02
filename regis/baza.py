import json
import sqlite3

def addUser(put,name,password):
    conn = sqlite3.connect(put)  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    sql = "SELECT * FROM albums WHERE title=?"
    cursor.execute(sql, [("Red")])
    for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY title"):
        data=json.loads(row[1])
    # with open(put, "r") as read_file:
    #     data = json.load(read_file)
    res = True
    for k,v in data["users"].items():
        if k == name:
            res=False
            break
    if res:
        data["users"][name]=[{},password]
    sql = """
    UPDATE albums 
    SET title = '
    """
    sql+=json.dumps(data)
    sql+='\''
    cursor.execute(sql)

    # Сохраняем изменения
    conn.commit()

    # with open(put, "w") as write_file:
    #     json.dump(data, write_file, indent=4)
    return res