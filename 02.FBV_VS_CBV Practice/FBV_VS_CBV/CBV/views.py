from django.shortcuts import render
from django.http import HttpResponse

from django.views import View    #For Class Based View we need to pass 'View' as a parameter 
 
from .forms import ContactForm   #forms.py ma vayeko form lai import gareko. (As this one is Form API of django.)
from django.http import HttpResponse


########################################## GET METHOD #######################################################################
# Create your views here.
#Function Based View(FBV) With get method(In FBV get method is automatically done no need to mention get method.)
def myview(request):
    return HttpResponse('<h1>Function Based View-GET.</h1>')

#Class Based View (CBV) with get method.(In CBV get method isn't taken automatically so we need to specify the method as well)
class MyView(View):
    name = 'Dipendra'
    def get(self, request): #In CBV we must specify GET,POST,PUT methods manually
        return HttpResponse('<h1>Class Based View-GET</h1>')
        # return HttpResponse(self.name) #We can even pass the values as like this.


#Let's See the advantage of using CBV as this will gives us facility of inhertance
class MyViewChild(MyView): #as a paramete MyView pathaunu vaneko tyo Class bata inherit garnu ho
    def get(self, request):
        return HttpResponse(self.name)


########################################## POST METHOD #######################################################################

#Function Based View POST Method
def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)        #making 'form' object.
        if form.is_valid():                     #validating the form.
            print(form.cleaned_data['name'])    #form data should always be get in 'cleaned_data'
            return HttpResponse('Thanks Your Form is Submitted.')
    
    else:   #This else is a 'Get' Method here while page loads one form will be displayed
        form = ContactForm()
    return render(request, 'CBV/contact.html', {'form':form})


#Class Based View POST Method

class ContactClassView(View):

    def get(self, request):         #In Class Based View we need to manually specify the method as get or post.
        form =ContactForm()
        return render(request, 'CBV/contact.html', {'form':form})
    
    def post(self, request):         #In Class Based View we need to manually specify the method as get or post.
        form = ContactForm(request.POST)        #making 'form' object.
        if form.is_valid():                     #validating the form.
            print(form.cleaned_data['name'])    #form data should always be get in 'cleaned_data'
            return HttpResponse('Thanks Your Form is Submitted.')
