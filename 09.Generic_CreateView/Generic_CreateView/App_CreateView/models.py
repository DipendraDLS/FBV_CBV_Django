from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)

    #If you want to see details of the particular records after submitting the form the we can use 'get_absolute_url' method
    def get_absolute_url(self):
        return reverse("detail", kwargs = {"pk":self.pk})   #kwargs will pass the 'id' of recently added user details to 'detail' url in urls.py

 