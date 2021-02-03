from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
import datetime
from institution.models import  InstitutionCategory, Field


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_speaker = models.BooleanField(default=False)
    is_institution = models.BooleanField(default=False)


    def __str__(self):
        return self.username



class Institution(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(InstitutionCategory, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    profile_pic = models.ImageField()
    address = models.CharField(max_length = 100, blank = True, null = True)
    city = models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    joined_date = models.DateField(auto_now_add=True)
    contact_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)
    email = models.EmailField()
    website = models.URLField()
    description = models.TextField(blank = True, null = True) 
    
    def __str__(self):
        return self.name





class Student(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    class_level = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    dob = models.DateField()
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    profile_pic = models.ImageField()
    def __str__(self):
        return f"{self.user.first_name}, {self.user.last_name}"






class Speaker(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    institution = models.ManyToManyField(Institution)
    phone_number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    field = models.ForeignKey(Field, on_delete = models.CASCADE)
    profile_pic = models.ImageField()
    def __str__(self):
        return f"{self.user.first_name}, {self.user.last_name}"

