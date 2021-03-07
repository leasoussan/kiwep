from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Speaker, Student, Representative, MyUser
from backend.models import Field,Level, Group
from todo.models import Task
from .managers import *


class Resource(models.Model):
    name = models.CharField(max_length=200) 
    link =  models.CharField(max_length=200)
    image = models.ImageField(default = 'image/default.png', upload_to='images/') 
    file_rsc = models.FileField(null=True, blank=True)
    text =  models.TextField() 
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE,  blank=True, null =True)
    
    objects = ResourceModelManager()

    def __str__(self):
        return f"Ressource Name : {self.name}"

    def get_absolute_url(self):
        return reverse("resource_detail", kwargs={"pk":self.pk})


    def get_resourceImg_or_default(self, default_path= 'images/default.png'):
        if self.image:
            return self.image.url
        return default_path


class Mission(models.Model):
    STAGE_CHOICE = [
        ('start', 'Start'),
        ('middle', 'Middle'),
        ('final', 'Final'),
    ]
    name = models.CharField(max_length=200)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    stage = models.CharField( max_length=10, choices=STAGE_CHOICE, default='start')
    description = models.TextField()
    resources = models.ManyToManyField(Resource)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    objects = MissionModelManager()

    def __str__(self):
        return f"Mission Name : {self.name}"

    def get_absolute_url(self):
        return reverse("mission_detail", kwargs={"pk":self.pk})





class Project(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    time_to_complet = models.PositiveIntegerField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Level, on_delete=models.CASCADE) 
    completed = models.BooleanField(default =False)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    mission = models.ManyToManyField(Mission, through = 'MissionsProject', blank =True)

    objects = ProjectModelManager()

    def __str__(self):
        return f"Project Name {self.pk} {self.name}"

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk":self.pk})



class MissionsProject(models.Model):
    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    mission =  models.ForeignKey(Mission, on_delete= models.CASCADE) 
    completed= models.BooleanField()
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    attributed_to = models.ForeignKey(Student, on_delete= models.CASCADE, related_name = "my_mission")
    


class Team(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    group_Institution = models.ForeignKey(Group, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Student)
    final_project = models.CharField(max_length=200)    
    manager = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name="team_manager")


 
    objects = TeamModelManager()

    def __str__(self):
        return f"Team Name : {self.name}"

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk":self.pk})


