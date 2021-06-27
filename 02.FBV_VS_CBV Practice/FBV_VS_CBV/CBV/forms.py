from django import forms
class ContactForm(forms.Form): #Using Form API not a model form
    name = forms.CharField(max_length=70)
    