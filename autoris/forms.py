from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Введите имя пользователя",max_length=50)  
    lastname  = forms.CharField(label="Введите пароль", max_length = 50)