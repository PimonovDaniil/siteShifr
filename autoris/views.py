from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .functions import handle_uploaded_file  
from .baza import checkUser


from .forms import StudentForm  


def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            if checkUser("regis/static/sql.txt",request.POST['firstname'],request.POST['lastname']):
                request.session['user'] = request.POST['firstname']
                return render(request,'autoris/homePage.html',{'form':student,"lol":"Вы успешно авторизировались!!!","user":request.session['user']})
            else:
                return render(request,'autoris/homePage.html',{'form':student,"lol":"Неверное имя пользователя или пароль","user":request.session['user']})
    else:  
        student = StudentForm()  
        return render(request,'autoris/homePage.html',{'form':student,"user":request.session['user']})  



 
