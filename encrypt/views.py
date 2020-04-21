# from django.shortcuts import render

# def index(request):
#     return render(request, 'encrypt/homePage.html')
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

from .functions import handle_uploaded_file  

from .forms import StudentForm  
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudentForm()  
        return render(request,'encrypt/homePage.html',{'form':student})  