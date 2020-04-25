from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .functions import handle_uploaded_file  
from .baza import addUser


from .forms import StudentForm  


def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            if addUser("regis/static/sql.txt",request.POST['firstname'],request.POST['lastname']):
                
                return render(request,'regis/homePage.html',{'form':student,"lol":"Вы успешно зарегистрировались!!!"})
            else:
                return render(request,'regis/homePage.html',{'form':student,"lol":"имя пользователя занято"})
    else:  
        student = StudentForm()  
        return render(request,'regis/homePage.html',{'form':student})  



# def index(request):
    # return render(request,'mainApp/homePage.html')
