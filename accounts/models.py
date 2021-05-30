from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
import datetime
from django.utils.translation import ugettext_lazy as _
from todo.models import Task, PersonalTask, TeamTask

from .managers import *


class Country(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
       return self.name



class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
       return self.name







class MyUser(AbstractUser):
    """ Basic User is the base of all users- using Django Implementation"""
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=30, blank = True, null = True)
    profile_pic = models.ImageField(default = 'profile/avatar.png', upload_to='media/profile/', blank = True, null = True)
    joined_date = models.DateField(auto_now_add=True, blank = True, null = True)
    city = models.ForeignKey(City,on_delete=models.CASCADE, null=True, blank=True)
    language_code = models.CharField(_('language'), choices = settings.LANGUAGES, default = 'en', max_length=50)
    is_student = models.BooleanField(default = False)
    is_speaker = models.BooleanField(default=False)
    is_representative = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()



    def __str__(self):
        return f"{self.id},{str(self.username)}, {self.email}"

    # get_usertype
    def get_user_type(self):
        user_type = {
        'representative':Representative,
        'speaker': Speaker,
        'student' : Student,
        }

        for key, value in user_type.items():

            if value.objects.filter(user=self).exists():
                return key


    def profile(self):
        types = [Representative,Speaker,Student]

        for value in types:
            qs =  value.objects.filter(user=self)
            if qs.exists():
                return qs.first()


    def profilepic_or_default(self, default_path='media/profile/avatar.png'):
        if self.profile_pic:
            return self.profile_pic.url
        return default_path


class Representative(models.Model):
    """ A Representative Profile if to be managing an Institution """
    user = models.OneToOneField(MyUser, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

    def get_absolute_url(self):
        return reverse('profile', kwargs={"pk":self.pk})

    # to be able to call it as class name in lower case
    def name(self):
        return self.__class__.__name__.lower()




class Student(models.Model):
    """ Student Profile """
    user = models.OneToOneField(MyUser, on_delete = models.CASCADE)
    class_level = models.ForeignKey('backend.Group', on_delete=models.CASCADE)
    field = models.ForeignKey('backend.Field',  on_delete=models.CASCADE)
    dob = models.DateField()
    softs_skills = models.ManyToManyField('content.Skills', through = 'backend.StudentSoftSkillRating', related_name= "student_skills_scores" )

    def __str__(self):
        return f"{self.user.username}, {self.user.last_name}"

    def get_absolute_url(self):
        return reverse('profile', kwargs={"pk":self.pk})


    def name(self):
        return self.__class__.__name__.lower()

    def tasks(self):
        personal_tasks = PersonalTask.objects.filter(user = self.user).values_list('task_ptr', flat=True)
        team_tasks = TeamTask.objects.filter(team__in = self.team_set.all()).values_list('task_ptr', flat=True)
        tasks = Task.objects.filter(id__in = list(personal_tasks) + list(team_tasks))
        # we cant add a queryset to queryset ---this is why we make them a list first
        return tasks
    # here before getting a student tasks I will have to do 2 queries that will be filtered in the parent table




class Speaker(models.Model):
    """ Speaker is anyone teaching a Course/ Lecturer"""
    user = models.OneToOneField(MyUser, on_delete = models.CASCADE)
    institution = models.ManyToManyField('backend.Institution')
    group = models.ManyToManyField('backend.Group')

    def __str__(self):
        return f"{self.user.username}, {self.user.last_name}"

    def get_absolute_url(self):
        return reverse('profile/', kwargs={"pk":self.pk})

    def name(self):
        return self.__class__.__name__.lower()

    def tasks(self):
        personal_tasks = PersonalTask.objects.filter(user = self.user).values_list('task_ptr', flat=True)
        team_tasks = TeamTask.objects.filter(team__in = self.team_manager.all()).values_list('task_ptr', flat=True)
        tasks = Task.objects.filter(id__in = list(personal_tasks) + list(team_tasks))
        # we cant add a queryset to queryset ---this is why we make them a list first
        return tasks
