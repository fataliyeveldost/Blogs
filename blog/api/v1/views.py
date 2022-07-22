from rest_framework.response import Response
from blog.models import Blog
from rest_framework.decorators import api_view
from.serializers import BlogSerializers,UserSerializers
from rest_framework import status,generics
from acount.models import CustomUser



class BlogListCreateApiView(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializers


class BlogDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializers
 
class UserListCreateApiView(generics.ListCreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializers

class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializers
        
        








