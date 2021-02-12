from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
import datetime
from backend.models import Institution, Group, Field

class Country(models.Model):
    name = models.CharField(max_length=100) 
    
    def __str__(self):
       return self.name


class City(models.Model): 
    name = models.CharField(max_length=100) 
    country = models.ForeignKey(Country, on_delete=models.CASCADE) 

    def __str__(self):
       return self.name



class UserType(models.Model):
    name =  models.CharField(max_length=100)
   
    def __str__(self):
       return self.name




class User(AbstractUser):
    email = models.EmailField()
    phone_number = models.CharField(max_length=30, blank = True, null = True)
    profile_pic = models.ImageField(blank = True, null = True)
    joined_date = models.DateField(auto_now_add=True, blank = True, null = True)
    city = models.ForeignKey(City,on_delete=models.CASCADE, null=True, blank=True) 
    usertype = models.ManyToManyField(UserType)


    def __str__(self):
        return self.name





class Representative(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name}, {self.institution.name}"







class Student(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    class_level = models.ForeignKey(Group, on_delete=models.CASCADE)
    Field = models.ForeignKey(Field,  on_delete=models.CASCADE)
    dob = models.DateField()
  
    def __str__(self):
        return f"{self.user.first_name}, {self.user.last_name}"




class Speaker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    institution = models.ManyToManyField(Institution)
    field = models.ForeignKey(Field, on_delete = models.CASCADE)
    group = models.ManyToManyField(Group)
    def __str__(self):
        return f"{self.user.first_name}, {self.user.last_name}"

