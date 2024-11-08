from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    usertype=models.CharField(max_length=200)

class Employee(models.Model):
    emp_id=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.IntegerField()
    address=models.CharField(max_length=200)
    phoneno=models.BigIntegerField()
    profilepic=models.ImageField(upload_to='images/', blank=True, null=True)
