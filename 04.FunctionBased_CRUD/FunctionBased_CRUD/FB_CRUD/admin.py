from django.contrib import admin
from .models import User
# Register your models here. 
# We need to register model in admin so that if we need to access the model from admin application then we can access it easily.

@admin.register(User)            #Decorator use garera 'User' model lai register gareko. 
class UserAdmin(admin.ModelAdmin):  # 'UserAdmin' -> Model admin class that inherits the 'admin.ModelAdmin'
    list_display = ('id', 'name', 'email', 'password')  #list of model fields that will be displayed in admin application.
