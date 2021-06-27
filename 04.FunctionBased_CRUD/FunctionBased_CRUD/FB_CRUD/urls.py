from django.urls import path
from FB_CRUD import views

urlpatterns = [
    path('', views.add_show, name='addandshow'),

    #For Deleting the data.This one is known as dynamic url.
    path('delete/<int:id>/', views.delete, name = 'delete'),

    path('<int:id>/', views.edit, name = 'edit')

    
]