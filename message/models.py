from django.urls import reverse
from django.db import models
from accounts.models import MyUser
from content.models import IndividualCollectiveMission, Team
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.

class Rating(models.Model):
    ACTION = (
        ('neutral', 'neutral'),
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)          
    action = models.CharField(max_length = 10, choices=ACTION)
    date = models.DateField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # 'content_type', 'object_id' are generic parameter for GenericContenteType


    def __str__(self):
        return f'rated by: {self.user.username}'

    # def get_absolute_url(self):
    #     return reverse("", kwargs={"pk":self.pk})






class CommentResponse(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    comment_text = models.TextField()


    def __str__(self):
        return f'posted by: {self.user.username}'

    # def get_absolute_url(self):
    #     return reverse("", kwargs={"pk":self.pk})




class CommentsTeam(models.Model):
    team = models.ForeignKey(Team,  on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    comment_text = models.TextField()
    responses = models.ManyToManyField(CommentResponse)

    def __str__(self):
        return f'posted by: {self.user.username}'

    def get_absolute_url(self):
        return reverse("team_comments_list", kwargs={"pk":self.pk})







class CommentsCollectiveMission(models.Model):
    mission = models.ForeignKey(IndividualCollectiveMission, on_delete=models.CASCADE)
    team_comments = models.ManyToManyField(CommentsTeam)
    vote = GenericRelation(Rating)

    def __str__(self):
        return f'Comments on Mission: {self.mission.title}'

    