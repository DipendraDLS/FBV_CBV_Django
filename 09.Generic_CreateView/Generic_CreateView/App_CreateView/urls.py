from django.urls import path
from App_CreateView import views

urlpatterns =[
    path('create/', views.StudentCreateView.as_view(), name = 'create'),
    path('thanks/', views.ThanksTemplateView.as_view(), name='thanks'),
    path('studetail/<int:pk>', views.StudentDetailView.as_view(), name = 'detail')
]

