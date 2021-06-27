from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views.generic import DetailView

from .models import Student

from django import forms
from .forms import StudentForm
# Create your views here.

# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['name', 'email', 'password']      #Fileds that is to be shown in template. default template name is 'student_form.html' i.e
#                                                 #(modelname_from.html) -> _form is suffix of CreateView.
                                                
#     # success_url = '/create/'                    #After clicking on submit button form will be redirect to 'create' url in urls.py.
#     # success_url = '/thanks/'                      #After clicking on submit button form will be redirect to 'thanks' which will
#                                                   #redirect it to new template using url in urls.py.

#     #There are 2 ways to give css or class to the form of CreateView
#     #1) using 'get_form' method
#     #2) Creating model form in forms.py

#     #1) 
#     def get_form(self):
#         form = super().get_form()
#         form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})   #If you inspect this in browser you will see the class 
#         form.fields['email'].widget = forms.TextInput(attrs = {'class':'myclass'})   #If you inspect this in browser you will see the class 
#         form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'myclass'})   #If you inspect this in browser you will see the class 
#         return form
    
########################################################################################################################################
    #2) See forms.py (this method of giving styling through class is more preffered one)
#This View was created to apply style or give {'class':'myclass'} in form fields using ModelForm in forms.py
class StudentCreateView(CreateView):    
    form_class = StudentForm            #ModelForm use gareko vayera yaha 'model=Student' vanera define garirakhna pardaina.
    template_name = 'App_CreateView/student_form.html'
    success_url = '/thanks/'


class ThanksTemplateView(TemplateView):
    template_name = 'App_CreateView/thanks.html'


class StudentDetailView(DetailView):
    model =Student




