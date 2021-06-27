from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        #Form ko field haru ma class or bootstrap class haru dinu parey we will use widgets
        widgets = {'name':forms.TextInput(attrs = {'class': 'myclass'}), 
                 'password':forms.PasswordInput(attrs={'class':'myclass'})}
                                                                                                
    