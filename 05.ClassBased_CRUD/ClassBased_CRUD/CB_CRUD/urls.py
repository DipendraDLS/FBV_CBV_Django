from django.urls import path
from CB_CRUD import views


urlpatterns = [
 

    path('', views.UserAddShowView.as_view(), name= 'addandshow'),

    #For Deleting the data.This one is known as dynamic url. Using Class Based View 
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name = 'delete'),

    #For Editing the data. 
    path('edit/<int:id>/', views.UserEditView.as_view(), name = 'edit')

    
]