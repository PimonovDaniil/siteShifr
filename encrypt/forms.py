from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Введите ключ шифрования(цифры)",max_length=50)  
    lastname  = forms.CharField(label="Введите сообщение которое будет зашифрованно", max_length = 5000)

    file      = forms.FileField() # for creating file input  