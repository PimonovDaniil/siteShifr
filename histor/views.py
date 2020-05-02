from django.shortcuts import render
import json
import sqlite3


def index(request):
    conn = sqlite3.connect("regis/static/sql.txt")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    sql = "SELECT * FROM albums WHERE title=?"
    cursor.execute(sql, [("Red")])
    for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY title"):
        data=json.loads(row[1])
    # with open("regis/static/sql.txt", "r") as read_file:
    #     data = json.load(read_file)
    return render(request, 'histor/homePage.html',{"user":request.session.get('user', ''),'log':data['users'][request.session['user']][0]})
