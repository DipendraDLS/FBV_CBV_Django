from django.shortcuts import render,HttpResponse
from .forms import ContactForm
from django.views.generic.edit import  FormView
from django.views.generic.base import TemplateView
# Create your views here.

class ContactFormView(FormView):

    template_name = 'App_FormView/contact.html'     #We need to define the template name in FormView
    form_class = ContactForm                        #forms.py ma define gareko 'ContactForm' ho . Jun form render garauna cha tyo form ko name lekhera render garauncha 
    success_url = '/thankyou/'                       #Form submit vayesakey pachi kata redirect garauni vanera 'url' name provide garuna parcha
    
    initial = {'name':'Ram', 'email': 'Ram@gmail.com'}      #If you want to show the initail values in form field whenever the form loads then
                                                            # you can use 'initial' attributes

    #Inorder to get the form field values that user has typed within the form:
    def form_valid(self,form):               #form API le provide greko method ho.
        print(form)                          #yo matrai garyo vani we get all the form field values but with all the html tags and attributes.
        print(form.cleaned_data['name'])     #so if you want only the values of form field then use 'cleaned_data'
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)
        #return HttpResponse('Msg Sent')    #you can even use HttpResponse to redirect the page.

    

class ThanksTemplateView(TemplateView):     #This View is created for 'success_url' which is redirect when user press submit button in 'ContactForm'
    template_name = 'App_FormView/thankyou.html'
    