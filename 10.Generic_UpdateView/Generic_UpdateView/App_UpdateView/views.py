from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.views.generic import TemplateView
from .models import Student

from django import forms
from .forms import StudentForm
# Create your views here.

# class StudentCreateView(CreateView):                #Create view is used to insert the data into database with the help of form.
#     model = Student                                 #models.py ma define vaye ko model ho.
#     fields = ['name', 'email', 'password']          # Forms ma kun kun field dekhauni ho tyo tyo yeta use huncha.
#     success_url = '/thanks/'                        # Form submit vaye paXi kun url ma redirect huni vanni kura ho.
#     template_name = 'App_UpdateView/create.html'    # Create.html ma forms dekhauncha. By default template name chai 'student_form.html linxa 
                                                    #i.e (modelname_form.html) '_form' is suffix for CreateView


#     #There are 2 ways to give css or class to the form of CreateView
#     #1) using 'get_form' method
#     #2) Creating model form in forms.py

#     #1) 
    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})   #If you inspect this in browser you will see the class 
    #     form.fields['email'].widget = forms.TextInput(attrs = {'class':'myclass'})   #If you inspect this in browser you will see the class 
    #     form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'myclass'})   #If you inspect this in browser you will see the class 
    #     return form
#     #NOTE: By giving class to Create form only it will not be added into Update form for that you need to add 'get_form' method in
#     #      StudentUpdateView as well
    
      #2) See forms.py (this method of giving styling through class is more preffered one)

 

# class StudentUpdateView(UpdateView):                # Yo view le CreateView kai form ma values haru display garaidinxa particualr 'id' ko so that 
                                                      # we can edit it. 
#     model = Student                                 # models.py ma define vaye ko model ho.
#     fields = ['name', 'email', 'password']          # Forms ma kun kun field dekhauni ho tyo tyo yeta use huncha.
#     success_url = '/thanksupdate/'                  # Form submit vaye paXi kun url ma redirect huni vanni kura ho.
#     template_name = 'App_UpdateView/create.html'    # create.html vanni mai form display vayerako huncha CreateView ko through so tei form ma 
                                                    # edit garnako lagi vanera field ma values haru display garaidincha.

#     #There are 2 ways to give css or class to the form of CreateView
#     #1) using 'get_form' method
#     #2) Creating model form in forms.py

#     #1) 
    # def get_form(self):
    #     form = super().get_form()
    #     form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})   #If you inspect this in browser you will see the class 
    #     form.fields['email'].widget = forms.TextInput(attrs = {'class':'myclass'})   #If you inspect this in browser you will see the class 
    #     form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'myclass'})   #If you inspect this in browser you will see the class 
    #     return form
#     #NOTE: By giving class to Create form only it will not be added into Update form for that you need to add 'get_form' method in
#     #      StudentUpdateView as well
    
########################################################################################################################################
#2) See forms.py (this method of giving styling through class is more preffered one)

#This View was created to apply style or give {'class':'myclass'} in form fields using ModelForm in forms.py
class StudentCreateView(CreateView):  
    form_class = StudentForm            # CreateView ma ModelForm ko through form display ma lyaunda 'model = Student' vanera specify garna pardaina
    template_name = 'App_UpdateView/create.html'
    success_url = '/thanks/'

class StudentUpdateView(UpdateView): 
    model  = Student                    # UpdateView maw ModelForm ko through form display garey pani or directly mathi line no. 36 ma garey
    form_class = StudentForm            # jasto garey pani 'model=Student' vanera specify garna nai parxa otherwise missing QuerySet error auncha.
    template_name = 'App_UpdateView/create.html'
    success_url = '/thanks/'



class ThanksTemplateView(TemplateView):             # Yo view le thanks.html template lai as a TemplateView ko through render garuna help garcha.
    template_name = 'App_UpdateView/thanks.html'


class ThanksUpdateTemplateView(TemplateView):       # Yo view le thanksupdate.html template lai as a TemplateView ko through render garuna help garcha.
    template_name = 'App_UpdateView/thanksupdate.html'



    