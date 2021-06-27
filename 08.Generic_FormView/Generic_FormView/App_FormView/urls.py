from django.urls import path
from App_FormView import views

urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name = 'contact'),
    path('thankyou/', views.ThanksTemplateView.as_view(), name='thankyou'),

]



