from django.shortcuts import render
import json


def index(request):
    with open("regis/static/sql.txt", "r") as read_file:
        data = json.load(read_file)
    return render(request, 'histor/homePage.html',{"user":request.session.get('user', ''),'log':data['users'][request.session['user']][0]})
