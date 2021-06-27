from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User        #model name that we have made in models.py
        fields = ['name', 'email', 'password']  #To show the form fields.

        #widget is used to style the form with bootstrap
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput( render_value = True , attrs={'class':'form-control'}), #render_value = True --> 'edit' button click password value pani tyo password field ma dekhauna ko lagi yo 'render_value' use huncha.

        }



