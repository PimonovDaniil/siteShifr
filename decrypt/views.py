from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

from .functions import deshifr
from .functions import handle_uploaded_file  

from .forms import StudentForm  
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            try:
                handle_uploaded_file(request.FILES['file'])  
                 
                return render(request,'decrypt/homePage.html',{'form':student,'lol':deshifr('decrypt/static/upload/'+request.FILES['file'].name,int(request.POST['firstname']))})
            except:
                return HttpResponse("Что-то вы ввели не так. Либо это мой косяк.")
    else:  
        student = StudentForm()  
        return render(request,'decrypt/homePage.html',{'form':student})  


# def index(request):
    # return render(request,'mainApp/homePage.html')