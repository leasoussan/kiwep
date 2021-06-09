from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts.models import *


class Level(models.Model):
    """ Level refers to a Poject Level, or Mission Level"""
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.name



class Field(models.Model):
    """ Fileds are area of subjects that an Institution, a Project, a Mission or a resource are part of"""
    SKILLS_TYPE = [
        ('soft', 'Soft Skills'),
        ('hard', 'Hard Skills')
    ]
    name = models.CharField(max_length=100)
    skills_type = models.CharField(max_length=50, choices = SKILLS_TYPE)

    def __str__(self):
        return f'{self.name} is a {self.skills_type} skill'



class InstitutionCategory(models.Model):
    """ Type of Institution, as School, university, organization etc..."""
    name = models.CharField(max_length=100)
    fields = models.ForeignKey(Field, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Institution(models.Model):
    """ Details of Institution """

    representative = models.OneToOneField(Representative, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    category = models.ForeignKey(InstitutionCategory, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default = 'profile/avatar.png', upload_to='media/profile/', blank = True, null = True)
    address = models.CharField(max_length = 100, null = True, blank = True)
    joined_date = models.DateField(auto_now_add=True)
    website = models.URLField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'



class Group(models.Model):
    """ Group is reference to a Classroom, or group of people part of same level one group can have few teams"""
    name = models.CharField(max_length = 100)
    number_of_participants = models.PositiveIntegerField()

    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class StudentSoftSkillRating(models.Model):
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    skill = models.ForeignKey('content.Skills', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    team = models.ForeignKey('content.Team', on_delete=models.CASCADE)
    comment = models.TextField()


    def __str__(self):
        return f'{self.student}, {self.rating}'
