from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _
# Create your models here.


class CustomUser(AbstractUser):
    name=models.CharField(max_length=22)

    def __str__(self):
        return self.username

