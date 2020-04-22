from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import mimetypes
import os

from .functions import handle_uploaded_file  
from .functions import shifr 

from .forms import StudentForm  
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            try:
                excel_file_name=shifr('encrypt/static/upload/'+request.FILES['file'].name,int(request.POST['firstname']),request.POST['lastname'])
                fp = open(excel_file_name, "rb");
                response = HttpResponse(fp.read());
                fp.close();
                file_type = mimetypes.guess_type(excel_file_name);
                if file_type is None:
                    file_type = 'application/octet-stream';
                response['Content-Type'] = file_type
                response['Content-Length'] = str(os.stat(excel_file_name).st_size);
                response['Content-Disposition'] = "attachment; filename=Encrypted_"+request.FILES['file'].name;
            
                return response;
            except:
                return HttpResponse("Что-то вы ввели не так. Либо это мой косяк.")
    else:  
        student = StudentForm()  
        return render(request,'encrypt/homePage.html',{'form':student})  