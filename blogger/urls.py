from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.userLogin, name='login'),
    path('signup', views.userSignup, name='signup'),
    path('logout', views.userLogout, name='logout'),
    path('generate-blog', views.generate_blog, name='generate_blog'),
    path('blog-list', views.blog_list, name='blog-list'),
    path('blog-details/<int:pk>', views.blog_details, name='blog-details'),
]