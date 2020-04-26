from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
import mimetypes
import json
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
                num=0
                with open("encrypt/static/upload/numfiles.txt",'r') as file_handler:
                    num=file_handler.read()
                num=str(int(num)+1)
                with open("encrypt/static/upload/numfiles.txt",'w') as file_handler:
                    file_handler.writelines(num)
                os.rename('encrypt/static/upload/'+request.FILES['file'].name, 'encrypt/static/upload/'+num+'.png')
                excel_file_name=shifr('encrypt/static/upload/'+num+'.png',int(request.POST['firstname']),request.POST['lastname'])
                fp = open(excel_file_name, "rb");
                response = HttpResponse(fp.read());
                fp.close();
                file_type = mimetypes.guess_type(excel_file_name);
                if file_type is None:
                    file_type = 'application/octet-stream';
                response['Content-Type'] = file_type
                response['Content-Length'] = str(os.stat(excel_file_name).st_size);
                response['Content-Disposition'] = "attachment; filename=Encrypted_"+num+".png";
                if request.session.get('user', "") != "":
                    with open("regis/static/sql.txt", "r") as read_file:
                        data = json.load(read_file)
                    data['users'][request.session['user']][0][request.FILES['file'].name]=request.POST['firstname']
                    with open("regis/static/sql.txt", "w") as write_file:
                        json.dump(data, write_file,indent=4)
                return response;
            except:
                return HttpResponse("Что-то вы ввели не так. Либо это мой косяк.")
    else:  
        student = StudentForm()  
        return render(request,'encrypt/homePage.html',{'form':student,"user":request.session.get('user', "")})  