from django.shortcuts import render


def index(request):
    return render(request, 'histor/homePage.html',{"user":request.session.get('user', '')})
