from django.urls import path
from.import views
urlpatterns = [
    path('blog/', views.BlogListCreateApiView.as_view() ),
    path('blog/<int:pk>', views.BlogDetailApiView.as_view()),

    path('users/', views.UserListCreateApiView.as_view(), name='user'),
    path('users/<int:pk>', views.UserDetailApiView.as_view(), name='user_detail'),
]
