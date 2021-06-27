from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

#This Function will add new item and show all records
def add_show(request):

    if request.method == 'POST':    # Jaba form ma 'Add' Button click huncha then post request auncha.
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
            form = StudentRegistration() #Form ma 'Add' button click garisakey pachi save vayesakera feri form load hunda typed value basi narakhos vanera yeuta blank form lai feri load gaarayeko.   
    else:
        form = StudentRegistration()
    students = User.objects.all()
    return render (request, 'FB_CRUD/addandshow.html', {'form': form, 'students': students})


#This function will delete records
def delete(request, id):
    if request.method == 'POST':
        del_record = User.objects.get(pk=id) #Particular user ko id ko through tyo particular user ko sabai value liyeko.
        del_record.delete()
        return HttpResponseRedirect('/')       #After deleting the user record it will redirect to the home page.

#This function will update the records.
def edit(request, id):
    if request.method == 'POST':
        edit_record = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=edit_record)  #Display vayeko form ma paritcular user ko preset value tanera tyo form ma display garaunba 'instance' ko use huncha.
        if form.is_valid():
            form.save()     #We can even use 'cleaned_data[]' method and get data one by one but this data is fetched from database where we have stored data in database in clean format while adding data so no need to use here cleaned_data
    else:
        edit_record = User.objects.get(pk=id)
        form = StudentRegistration(instance=edit_record)


    return render(request, 'FB_CRUD/updatestudent.html', {'form':form})