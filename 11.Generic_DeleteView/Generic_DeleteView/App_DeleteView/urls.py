from django.urls import path
from App_DeleteView import views

urlpatterns = [
    path('create/', views.StudentCreateView.as_view(), name='create'),
    
    path('thanks/', views.ThanksTemplateView.as_view(), name='thanks'),

    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update'),

    path('thanksupdate/', views.ThanksUpdateTemplateView.as_view(), name='thanksupdate'),

    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete'),

    
    path('thanksdelete/', views.ThanksDeleteTemplateView.as_view(), name='thanksdelete'),

]

