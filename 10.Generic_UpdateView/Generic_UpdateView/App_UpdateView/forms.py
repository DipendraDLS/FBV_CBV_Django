from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        widgets = {'name':forms.TextInput(attrs = {'class': 'myclass'}), 
                  'password':forms.PasswordInput( render_value = True, attrs={'class':'myclass'})}

                    #render_value =Ture means update garni bela passwordfield ma ni kei value haru dekhaidiyos vanera ho.
                    # Yo rakhena vani update garni bela aru form field ma chai purano value haru dekhai rakhni
                    # but password field ma chai khali field matra display huni tara purano value nadekhauni hunxa.
                    # So 'render_value = True rakhna jaroori cha.
                

                