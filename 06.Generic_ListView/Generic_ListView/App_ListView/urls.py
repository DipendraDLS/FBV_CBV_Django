from django.urls import path
from App_ListView import views

urlpatterns = [
    path("", views.StudentList.as_view(), name="student")
]

