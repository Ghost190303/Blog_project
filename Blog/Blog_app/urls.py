from .import views
from django.urls import path


urlpatterns = [
    path('', views.Blog_list, name='Blog_list'),
    path('create/', views.Blog_create, name='Blog_create'),
    path('<int:Blog_id>/edit/', views.Blog_edit, name='Blog_edit'),
    path('<int:Blog_id>/delete/', views.Blog_delete, name='Blog_delete'),
    path('registor/', views.registor, name='registor'),
    # path('forgetpassword/',views.forget_password, name='forgetpassword')

]
