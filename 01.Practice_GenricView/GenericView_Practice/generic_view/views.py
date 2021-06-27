from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
#Class Based Generic View (This one is the best method)
class StaticView(TemplateView):
   template_name = "static_using_view.html"

#Function Based Genric View 
# def static(request):
#    context = {}
#    return render(request, 'static_using_view.html', context)


