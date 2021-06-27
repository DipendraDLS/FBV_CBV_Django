from django.urls import path
from App_DetailView import views

urlpatterns = [
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name="studentdetails"),
]



