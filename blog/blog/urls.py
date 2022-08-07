from django import views
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.all_blogs, name='all_blogs'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_blog, name='create_blog'),
    path('update-blog/<int:pk>/', views.update_blog, name='update_blog'),
    path('delete-blog/<int:pk>/', views.delete_blog, name='delete_blog'),
    path('api_v1_blog_create/', views.BlogListCreateApiView.as_view(), name='api_v1_blog'),
    path('api_v1_user_create/', views.UserListCreateApiView.as_view(), name='api_v1_user'),

]
