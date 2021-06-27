from django.urls import path
from CBV import views

urlpatterns = [

    #For Function Based View
    path('fbv/', views.myview, name= 'fbv'),

    #For Class Based View
    path('cbv/',views.MyView.as_view() , name= 'cbv'),

    #For Class Based View Child Class
    path('cbv_child/',views.MyViewChild.as_view() , name= 'cbv_child'),

    #For Function Based View POST Method.
    path('contactfun/', views.contactfun, name='contactfun'),

    #For Class Based View POST Method.
    path('contact_cbv/', views.ContactClassView.as_view(), name = 'contact_cbv'),

]

