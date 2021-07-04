from django.db import models

# Create your models here.
class AccountUser(models.Model):
    username=models.CharField(max_length=255,unique=True)
    email=models.CharField(max_length=255,unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    