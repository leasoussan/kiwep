from django.urls import reverse
from django.db import models
# from accounts.models import MyUser
from django.forms import modelform_factory
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType





class Rating(models.Model):
    ACTION = (
        ('neutral', 'neutral'),
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    user = models.ForeignKey('accounts.MyUser', on_delete=models.CASCADE)
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






class Comment(models.Model):
    user = models.ForeignKey('accounts.MyUser', on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    comment_text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    replies = GenericRelation('Comment')


    def __str__(self):
        return f'posted by: {self.user.username}'

    # def get_absolute_url(self):
    #     return reverse("", kwargs={"pk":self.pk})
    


class Discussion(Comment):
    title = models.CharField(max_length=50)


    def __str__(self):
        return f'iscrussion title: {self.title}'

    def get_absolute_url(self):
        return reverse("team_comments_list", kwargs={"pk":self.pk})








    # This model rewrite the models.Model
class DiscussionModel(models.Model):
    discussions = GenericRelation(Discussion)

    class Meta:
        abstract = True


    def discussion_form(self):

        return modelform_factory(Discussion, fields=['title','comment_text'])()