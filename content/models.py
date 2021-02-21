from django.db import models
from django.urls import reverse
from django.conf import settings
from accounts.models import Speaker, Student
from backend.models import Field,Level, Group
from todo.models import Task



class Resource(models.Model):
    name = models.CharField(max_length=200) 
    link =  models.CharField(max_length=200)
    text =  models.TextField() 

    def __str__(self):
        return f"Ressource Name : {self.name}"




class Mission(models.Model):
    name = models.CharField(max_length=200)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    description = models.TextField()
    completed = models.BooleanField
    resources = models.ManyToManyField(Resource)

    def __str__(self):
        return f"Mission Name : {self.name}"




class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    time_to_complet = models.PositiveIntegerField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Level, on_delete=models.CASCADE)
    mission = models.ManyToManyField(Mission)
    completed = models.BooleanField(default =False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Project Name {self.pk} {self.name}"


    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk":self.pk})


class Team(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    group_Institution = models.ForeignKey(Group, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Student)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    final_project = models.CharField(max_length=200) 

    def __str__(self):
        return f"Team Name : {self.name}"




