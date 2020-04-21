from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

from .functions import handle_uploaded_file  
from .functions import shifr 

from .forms import StudentForm  
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            try:
                shifr('encrypt/static/upload/'+request.FILES['file'].name,int(request.POST['firstname']),request.POST['lastname'])
                return HttpResponse("File uploaded successfuly")  
            except:
                return HttpResponse("Что-то вы ввели не так. Либо это мой косяк.")
    else:  
        student = StudentForm()  
        return render(request,'encrypt/homePage.html',{'form':student})  