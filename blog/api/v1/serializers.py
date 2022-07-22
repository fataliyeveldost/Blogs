from pyexpat import model
from blog.models import Blog
from rest_framework import serializers 
from acount.models import CustomUser

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields="__all__"