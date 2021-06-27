from django.urls import path
from django.views.generic import TemplateView
from generic_view.views import StaticView
from . import views


urlpatterns = [
    #when 127.0.0.1:8000 is loaded 
    path("",TemplateView.as_view(template_name = 'show.html')),

    #when 'show Directly' button is clicked
    path('show_direct/',TemplateView.as_view(template_name = 'static_directly.html'), name = "show_direct"),

    #when 'Show Using View' button is clicked. (With the help of Class Based Generic View.(CBVs))
    path('show_using_view/', StaticView.as_view(), name = "show_using_view"),

    #when 'Show Using View' button is clicked.(With the help of Function Based View(FBVs))
    # path('show_using_view/', views.static, name = "show_using_view")

]

