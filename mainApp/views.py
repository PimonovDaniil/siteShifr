from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html',{"lol":request.session.get('user', '')})

def exit(request):
    request.session['user'] = ""
    return render(request, 'mainApp/homePage.html',{"lol":request.session.get('user', '')})