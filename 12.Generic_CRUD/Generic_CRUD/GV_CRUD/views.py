from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import User

from .forms import UserRegistration

# Create your views here.

############################## Generic CreateView & ListView ################################################

class UserCreateAndListView(CreateView, ListView): #Both types of different generic view can also be passed at same class.

    #from below for CreateView
    form_class = UserRegistration
    template_name = 'GV_CRUD/addandshow.html'
    success_url = '/'

    #From below for List View
    model = User
    context_object_name = 'users'

 
############################## Generic DetailView ##############################################################
class UserDetailView(DetailView):
    model = User
    template_name = 'GV_CRUD/userdetails.html'
    context_object_name = 'users'

################################ Generic DeleteView ###############################################################
class UserDeleteView(DeleteView):
    model = User
    template_name = 'GV_CRUD/confirm_delete.html' 
    success_url = '/'

################################ Generic UpdateView ###################################################################
class UserUpdateView(UpdateView): 
    model  = User                     
    form_class = UserRegistration
    template_name = 'GV_CRUD/update.html'
    success_url = '/'