from django.db import models
from django.conf import settings




class Field(models.Model):
    name = models.CharField(max_length=100) 


    def __str__(self):
        return self.name
    




class InstitutionCategory(models.Model):
    name = models.CharField(max_length=100) 
    fields = models.ForeignKey(Field, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Institution(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(InstitutionCategory, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    profile_pic = models.ImageField()
    address = models.CharField(max_length = 100, blank = True, null = True)
    city = models.CharField(max_length = 50,null=True, blank=True)
    country = models.CharField(max_length = 50,null=True, blank=True)
    joined_date = models.DateField(auto_now_add=True)
    contact_name = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)
    email = models.EmailField()
    website = models.URLField()
    description = models.TextField(blank = True, null = True) 
    
    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length = 100)
    number_of_participants = models.PositiveIntegerField()
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.name