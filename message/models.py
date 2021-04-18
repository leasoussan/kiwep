from django.db import models
from accounts.models import MyUser
from content.models import CollectiveProjectMission, Team

# Create your models here.

class Comment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'posted by: {self.user.username}'


class TeamCommentsBoard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)
    
    def __str__(self):
        return f'Comments board of Team: {self.team.name}'


class MissionComments(models.Model):
    mission = models.ForeignKey(CollectiveProjectMission, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)  

    def __str__(self):
        return f'Missions Comments {self.mission.title}'
