from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

from django.views.generic import TemplateView, RedirectView
from django.views import View

# Create your views here.
########################################################## (USING TEMPLATE VIEW) ###########################################################
#Class Based View 
#This Class View will add new record and shows all records
class UserAddShowView(TemplateView):
    template_name = 'CB_CRUD/addandshow.html'   #Template lai render garauna cha vani we need to use like this is Class Based View

    #Class Based View use garda yedi context send garna cha vani we need to use method provided by 'TemplateView' i.e def get_context_data(self, *args, **kwargs):
   
    #Below one is 'get' method.
    def get_context_data(self, *args, **kwargs):    #Hamiley TemplateView ko method lai overwrite gareko ho .
        context = super().get_context_data(**kwargs) #Kwargs le url ma aayeko value lai as a dictionary return gardincha.
        form = StudentRegistration()            # 'form' is an object of 'StudentRegistration' Class
        students = User.objects.all()           #Getting all the records from database
        context = {'students':students, 'form':form}
        return context
    
    #Below one is POST method
    def post(self,request):
        form = StudentRegistration(request.POST)    # 'form' is an object of 'StudentRegistration' class
        if form.is_valid():
            #There are two method to save the form data:
            #1) using form object i.e --> form.save()
            #2) getting each data one by one as in cleaned_data and storing it into variables and then save to database with the help of model.  

            #Method 1)
            # form.save()

            #Method 2) This method is the best way to store data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            register = User(name=name, email=email, password=password)
            register.save()
            return HttpResponseRedirect('/')


########################################################## (USING REDIRECT VIEW) #################################################################

#This Class will delete records
class UserDeleteView(RedirectView):
    url = '/'   #RedirectView Use gareko vayera delete ko kam vayesakey paxi redirect kata garni vanera yesari direct use garna pauncha.
    
    def get_redirect_url(self, *args, **kwargs):    #This method is given by 'RedirectView' so yeslai overrride gareko.
        # print(kwargs)         #'kwargs' ma 'Delete' button press garda delete garnu parni record ko id aayera baseko huncha in a dictionary format.       
        get_id =  kwargs['id']  #kwargs dictionary ma {'id': id} yesari ayerako huncha so tyo 'id' key ko throught value get gareko
        del_record = User.objects.get(pk=get_id)    #Particular 'id' ko record lai query lagayera get gareko
        del_record.delete()                         #tyo id ko record lai delete gardiyeko.
        return super().get_redirect_url(*args, **kwargs)    #get_redirect_url method le return yehi nai garcha.




########################################################## (USING  VIEW) #################################################################

#This Class will update the records.
class UserEditView(View):
    def get(self, request, id):     #django ko View mathi import gareko cha so tesley provide gareko get method ho.
                                    #'edit button click garda 'id' auncha.

        edit_record = User.objects.get(pk=id)
        form = StudentRegistration(instance=edit_record)
        return render(request, 'CB_CRUD/updatestudent.html', {'form':form})
    
    def post(self, request, id):
        edit_record = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=edit_record)  #Display vayeko form ma paritcular user ko preset value tanera tyo form ma display garaunba 'instance' ko use huncha.
        if form.is_valid():
            form.save()     #We can even use 'cleaned_data[]' method and get data one by one but this data is fetched from database where we have stored data in database in clean format while adding data so no need to use here cleaned_data
            return HttpResponseRedirect('/')    #form update vayesakey pachi home page ma redirect gardiyeko.