from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Speaker, Student, Representative, MyUser
from backend.models import Field,Level, Group
from todo.models import Task
from .managers import *
# this is like a trans tag - just for the backend 
from django.utils.translation import ugettext_lazy as _


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



class Subjects(models.Model):
    name = models.CharField(max_length= 100)

    
    def __str__(self):
        return f"Subject{self.name}"

    

class RequiredSkills(models.Model):
    name  = models.CharField(max_length= 100)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return f"SubjectRequired sikills {self.subject}, {self.name}"



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



class SkillsAcquired(models.Model):
    name  = models.CharField(max_length= 100)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Subject{self.subject}, {self.name}"



class Project(models.Model):

    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    required_skills = models.ManyToManyField(RequiredSkills, blank=True)
    acquried_skils = models.ManyToManyField(SkillsAcquired, blank=True)
    time_to_complet = models.PositiveIntegerField()
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Level, on_delete=models.CASCADE) 
    completed = models.BooleanField(default =False)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    mission = models.ManyToManyField(Mission, blank =True)
    points = models.PositiveIntegerField()
    
    
    objects = ProjectModelManager()

    class Meta:
        verbose_name = _('project')

        verbose_name_plural = _('projects')

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
    participants = models.ManyToManyField(Student, blank = True )
      
    manager = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name="team_manager")
    missions = models.ManyToManyField(Mission, through = 'TeamProjectMission')        


 
    objects = TeamModelManager()

    def __str__(self):
        return f"Team Name : {self.name}"

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk":self.pk})


    # def get_available_mission(self):

    #     return TeamProjectMission.objects.filter(team=self, attributed_to = None)


class TeamProjectMission(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)        
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    attributed_to = models.ForeignKey(Student, on_delete= models.CASCADE, related_name = "my_missions", blank = True, null=True)
    completed= models.BooleanField(default=False)
    response_text = models.TextField(blank=True)
    response_file = models.FileField(null=True, blank=True)
    accepted = models.BooleanField(default=False)

    objects = TeamProjectMissionModelManager()


    def __str__(self):
        return f"Missions of Team: {self.team}"


    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk":self.pk})