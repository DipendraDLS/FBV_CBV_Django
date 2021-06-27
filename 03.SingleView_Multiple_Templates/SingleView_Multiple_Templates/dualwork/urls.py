from django.urls import path
from dualwork import views

urlpatterns = [
    # For multiple template to render using same view in Function Based View
    # We need to pass the template name from here otherwise we can't render multiple template using same view 
    # (i.e dual functionality with same view.)
    path('newsfun1/', views.newsfun, {'template_name' :'dualwork/news1.html'}, name = 'newsfun1'),
    path('newsfun2/', views.newsfun, {'template_name' :'dualwork/news2.html'}, name = 'newsfun2'),


    # For multiple template to render using same view in Class Based View
    # We need to pass the template name from here otherwise we can't render multiple template using same view 
    # (i.e dual functionality with same view.)
    path('newsclass1/', views.NewsClassView.as_view(template_name = 'dualwork/news1.html') ,  name = 'newsclass1'),
    path('newsclass2/', views.NewsClassView.as_view(template_name = 'dualwork/news2.html') , name = 'newsclass2'),

]