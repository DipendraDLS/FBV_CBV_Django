from django.urls import path
from GV_CRUD import views

urlpatterns = [
    path('', views.UserCreateAndListView.as_view(), name='home'),

    path('user_details/<int:pk>/', views.UserDetailView.as_view(), name='user_details'),

    path('user_delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),

    path('user_update/<int:pk>/', views.UserUpdateView.as_view(), name='user_update'),



]