from pyexpat import model
from django.db import models
from acount.models import CustomUser
# Create your models here.



class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='blog')

    def __str__(self) -> str:
        return self.title