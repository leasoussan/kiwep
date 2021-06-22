from django.db import models
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import Speaker, Student, Representative, MyUser
from backend.models import Field, Level, Group
from django.db import models
from django.contrib import messages
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save
from django.contrib.contenttypes.fields import GenericRelation
from datetime import datetime, timedelta





from .managers import *
# this is like a trans tag - just for the backend 
from django.utils.translation import ugettext_lazy as _
# signals
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed, pre_delete

from django.utils import timezone
from message.models import DiscussionModel,AnswerModel



class Resource(DiscussionModel):
    name = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    image = models.ImageField(default = 'media/image/default.png', upload_to='images/')
    file_rsc = models.FileField(null=True, blank=True)
    text = models.TextField()
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE,  blank=True, null =True)
    objects = ResourceModelManager()

    def __str__(self):
        return f"Ressource Name : {self.name}"

    def get_absolute_url(self):
        return reverse("resource_detail", kwargs={"pk":self.pk})


    def get_resourceImg_or_default(self, default_path= 'media/images/default.png'):
        if self.image:
            return self.image.url
        return default_path


class Skills(models.Model):
    name = models.CharField(max_length= 100)
    field = models.ManyToManyField(Field)


    def __str__(self):
        return f"Subject{self.name}"


class Project(DiscussionModel):
    """ Model Of Project - independent of a Team - a project is reusable to each team his own """

    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    required_skills = models.ManyToManyField(Skills, related_name="required_skills")
    acquired_skills = models.ManyToManyField(Skills)
    time_to_complete = models.PositiveIntegerField()
    field = models.ManyToManyField(Field)
    resources = models.ManyToManyField(Resource, blank=True)
    difficulty = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    is_template = models.BooleanField(default=False)
    is_global = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)

    objects = ProjectModelManager()

    class Meta:
        verbose_name = _('project')

        verbose_name_plural = _('projects')

    def __str__(self):
        name = f"Project Name {self.pk} {self.name} "
        if self.is_template:
            name += "Template"
        return name

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})





class Mission(AnswerModel):
    STAGE_CHOICE = [
        ('start', 'Start'),
        ('middle', 'Middle'),
        ('final', 'Final'),
    ]

    RESPONSE_TYPE = [
        ('link', 'Link'),
        ('video', 'Video'),
        ('doc', 'Document'),
        ('power_p', 'Power Point'),
        ('image', 'image'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    stage = models.CharField(max_length=10, choices=STAGE_CHOICE, default='start')
    response_type = models.CharField(max_length=200, choices=RESPONSE_TYPE, default=None)
    name = models.CharField(max_length=200)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, blank= True, null= True)
    description = models.TextField()
    resources = models.ManyToManyField(Resource, blank=True)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    acquired_skill = models.ManyToManyField(Skills, blank =True)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=timezone.now)

    # objects = MissionModelManager()

    class Meta:
        abstract = True

    def __str__(self):
        return f"Mission Name : {self.name}"


class MissionValue(models.Model):
    percentage = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    hard_skills = models.ManyToManyField(Skills, through='HardSkillsRating', blank=True)
    content_type = models.ForeignKey(ContentType, default=None, null=True, on_delete=models.SET_NULL, related_name='activity_logs')
    object_id = models.PositiveIntegerField()
    object = GenericForeignKey(ct_field="content_type", fk_field="object_id")

# Teacher decides how much the mission distribution of points there is in the mission- according to skills ni the mission
# could be 100% of one skill and few % if many skills
#
class HardSkillsRating(models.Model):
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)
    project_mission = models.ForeignKey(MissionValue, on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)


class IndividualMission(Mission):
    """ an Individuall Mission is a Mission that has to be done by one team Member,
        so this mission can be claimed """

    attributed_to = models.ForeignKey(Student, on_delete= models.CASCADE,  related_name = "my_missions", blank = True, null=True)
    hard_skill_rating = GenericRelation(MissionValue)

    objects = IndividualMissionModelManager()


    def __str__(self):
        return f"Missions of project: {self.project.name}"


    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk":self.pk})


    def get_update_url(self):
        """ To """
        return reverse('update_individual_mission', kwargs={"pk":self.pk})



class CollectiveMission(Mission):
    """
    This mission has to be done by each participants of a team.
    Therefore each participants will have this mission attributed to him """
    attributed_to = models.ManyToManyField(Student, through='IndividualCollectiveMission',
                                           related_name="my_team_missions", blank=True)
    hard_skill_rating = GenericRelation(MissionValue)
    objects = CollectiveMissionModelManager()

    def __str__(self):
        return f"Missions of Team: {self.project.team}"

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        """ To get the link to the update"""
        return reverse('update_collective_mission', kwargs={"pk":self.pk})




class IndividualCollectiveMission(AnswerModel):
    """Through table > a Custom ManyToMany Table to manage the Collective mission status  """

    attributed_to = models.ForeignKey(Student, on_delete= models.CASCADE , related_name = "individual_team_mission")
    parent_mission = models.ForeignKey(CollectiveMission, on_delete= models.CASCADE)




    def __str__(self):
        return f"Team Project Mission of Team: {self.parent_mission.project.team}"


    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk":self.pk})





class Team(DiscussionModel):
    """ a Team Model is to manage a Project per Team- Creating a team is allowing the Speaker to  
    Manage one or few people on a Project"""
    name = models.CharField(max_length=200)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    group_Institution = models.ForeignKey(Group, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Student, blank = True )
    manager = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    project_completed = models.BooleanField(null=True, blank = True)


    objects = TeamModelManager()


    def __str__(self):
        return f"Team Name : {self.name}"

    def get_absolute_url(self):
        return reverse("team_detail", kwargs={"pk":self.pk})

    def due_date(self,):
        if self.project:
            due_date = self.start_date + timedelta(days=self.project.time_to_complete)

            return due_date

    def days_left(self):
        if self.project:
            now = datetime.now().date()
            days_left = (self.due_date() - now)
            return days_left.days

# def check_date(sender, instance, *args, **kwargs):
#         if instance.start_date > instance.due_date:
#             raise ValueError('Start date must be less than end date')

# pre_save.connect(check_date, sender=Team)