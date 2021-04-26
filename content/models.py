from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Speaker, Student, Representative, MyUser
from backend.models import Field,Level, Group

from .managers import *
# this is like a trans tag - just for the backend 
from django.utils.translation import ugettext_lazy as _
# signals
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed

from django.utils import timezone


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


class Skills(models.Model):
    name  = models.CharField(max_length= 100)
    field = models.ManyToManyField(Field)

    
    def __str__(self):
        return f"Subject{self.subject}, {self.name}"





class Mission(models.Model):
    MISSION_TYPE = [
        ('s_m', 'Student Mission'),
        ('t_m', 'Team Mission'),

   ] 
    RESPONSE_TYPE = [
        ('link', 'Link'),
        ('video', 'Video'),
        ('doc', 'Document'),
        ('power_p' ,'Power Point' ),
        ('image' ,'image' ),
    ]

    mission_type = models.CharField(max_length=200, choices= MISSION_TYPE, default='s_m' )
    response_type = models.CharField(max_length=200, choices=RESPONSE_TYPE, default=None)
    name = models.CharField(max_length=200)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank= True, null= True)
    description = models.TextField()
    resources = models.ManyToManyField(Resource)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    acquried_skill = models.ManyToManyField(Skills, blank =True)


    objects = MissionModelManager()

    def __str__(self):
        return f"Mission Name : {self.name}"

    def get_absolute_url(self):
        return reverse("mission_detail", kwargs={"pk":self.pk})


class Project(models.Model):

    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    required_skills = models.ManyToManyField(Skills, related_name="required_skills")
    acquried_skills = models.ManyToManyField(Skills)
    time_to_complet = models.PositiveIntegerField()
    field = models.ManyToManyField(Field)
    difficulty = models.ForeignKey(Level, on_delete=models.CASCADE) 
    completed = models.BooleanField(default =False)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    missions = models.ManyToManyField(Mission, blank =True)
    points = models.PositiveIntegerField()
    
    
    objects = ProjectModelManager()

    class Meta:
        verbose_name = _('project')

        verbose_name_plural = _('projects')

    def __str__(self):
        return f"Project Name {self.pk} {self.name}"

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk":self.pk})

# here we are writing a receiver listen to signal and what to do when you hear what to do 
# 1_ post save + intereste to know all post save
# 2_ to hear from the Project - the Project is SENDER of the signal 
# 3
@receiver(post_save,sender=Project )
def email_new_project_event(sender, created, instance, **kwargs):
    if created: 
        pass
    # here I can chose what to do 


            
# m2m_changed have acition attribute that have to be handled 
# reverse : if we want to remove a project from a mission (and not mission form a project) - as it's a many to many relation 

@receiver(m2m_changed, sender=Project.missions.through)
def update_team_mission_attribution(instance, reverse, action , pk_set, **kwargs):
    if not reverse:
        if action == 'post_remove':
            CollectiveProjectMission.objects.filter(team__in=instance.team_set.all()).filter(mission_id__in=pk_set).delete()

        elif action == 'post_add':
            project = instance
            for team in project.team_set.all():
                for mission in project.mission.filter(id__in= pk_set):
                    CollectiveProjectMission.objects.create(mission=mission, team=team )




class Team(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start_date = models.DateField()
    due_date = models.DateField()
    group_Institution = models.ForeignKey(Group, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Student, blank = True )    
    manager = models.ForeignKey(Speaker, on_delete=models.CASCADE, related_name="team_manager")
    individual_missions = models.ManyToManyField(Mission, through = 'IndividualProjectMission') 
    team_missions =  models.ManyToManyField(Mission, through = 'CollectiveProjectMission', related_name ='team_missions') 
    
    project_completed = models.BooleanField(null=True, blank = True)

 
    objects = TeamModelManager()



    def __str__(self):
        return f"Team Name : {self.name}"

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk":self.pk})


@receiver(post_save, sender=Team)
def team_mission_attribution(sender, created, instance, *args, **kwargs):
    if created: 
        for mission in instance.project.missions.all():
            if mission.mission_type == 's_m':
                IndividualProjectMission.objects.create(mission=mission,team=instance,due_date=timezone.now())
            
            elif mission.mission_type == 't_m':
                CollectiveProjectMission.objects.create(mission=mission, team=instance,due_date=timezone.now())

            

# created check if it's new or note
# instance is team as we have the signal on the team creat missions project so this is the instance we are dealing with 

# related name is to change the default access from othermodel_set to the ne realted name.
# for ex in Team: we have FK to project, by default to access all team with the same project we ll go from 
# project.team_set.all>>.the related name >> if related name == teams ; then we all do project.teams.all 
# it's like a tag /lable to call without needing to go backward.

class IndividualProjectMission(models.Model):
    STAGE_CHOICE = [
        ('start', 'Start'),
        ('middle', 'Middle'),
        ('final', 'Final'),
    ]
    stage = models.CharField( max_length=10, choices=STAGE_CHOICE, default='start')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)        
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=timezone.now)
    attributed_to = models.ForeignKey(Student, on_delete= models.CASCADE,  related_name = "my_missions", blank = True, null=True)
    completed= models.BooleanField(default=False)
    response_comment = models.TextField(blank=True)
    response_file = models.FileField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
    
    objects = IndividualProjectMissionModelManager()


    def __str__(self):
        return f"Missions of Team: {self.team}"


    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk":self.pk})




# ex make your resume 

class CollectiveProjectMission(models.Model):
    """
    This mission is collective for all participants and is able to be managed by each participants 
     """
    STAGE_CHOICE = [
        ('start', 'Start'),
        ('middle', 'Middle'),
        ('final', 'Final'),
    ]
    stage = models.CharField( max_length=10, choices=STAGE_CHOICE, default='start')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)        
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=timezone.now)
    attributed_to = models.ManyToManyField(Student, through = 'IndividualCollectiveProjectMission' , related_name = "my_team_missions", blank = True)
    completed= models.BooleanField(default=False)
    response_comment = models.TextField(blank=True)
    response_file = models.FileField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
    
    objects = CollectiveProjectMissionModelManager()


    def __str__(self):
        return f"Missions of Team: {self.team}"


    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk":self.pk})


@receiver(m2m_changed, sender=CollectiveProjectMission.attributed_to)
def assign_collective_mission(instance, reverse, action , pk_set, **kwargs):

    if not reverse:
    # instance is a collectiveprojectmission pk_set of Students - only true if we are inside the IF 
    # reverse is indication of the relation of what we are saving 
        if action == 'post_remove':
            IndividualCollectiveProjectMission.objects.filter(attributed_to__in= instance.assigned_to.filter(id__in=pk_set)).delete()

        elif action == 'post_add':
            for pk in pk_set:
                IndividualCollectiveProjectMission.objects.create(parent_mission=instance, attributed_to_id=pk)
                




class IndividualCollectiveProjectMission(models.Model):
    """ Her is about the model   """
    attributed_to = models.ForeignKey(Student, on_delete= models.CASCADE , related_name = "individual_team_mission")
    parent_mission = models.ForeignKey(CollectiveProjectMission, on_delete= models.CASCADE)
    completed= models.BooleanField(default=False)
    response_comment = models.TextField(blank=True)
    response_file = models.FileField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
  

    def __str__(self):
        return f"Team Project Mission of Team: {self.team}"


    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk":self.pk})
