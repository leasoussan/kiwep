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



class Answer(models.Model):
    STATUS_CHOICES =[
        ('w_r', 'Waiting Review'),
        ('u_r','Under Review'),
        ('a', 'Accepted'),
        ('r', 'Rejected'),
        ('c', 'See Comments'),
    ]
    response_comment = models.TextField(blank=True)
    response_file = models.FileField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='w_r')

    def __str__(self):
        return f'answe by: {self.user.username}'




class Comment(models.Model):
    user = models.ForeignKey('accounts.MyUser', on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    comment_text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    replies = GenericRelation('Comment')


    class Meta:
        ordering = ['date_posted']

    def __str__(self):
        return f'posted by: {self.user.username}'






class Discussion(Comment):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f'iscrussion title: {self.title}'

    def get_absolute_url(self):
        return reverse("team_comments_list", kwargs={"pk":self.pk})



    def comment_form(self):
        from .forms import AddCommentForm
        ct = ContentType.objects.get_for_model(self)
        return AddCommentForm(initial={'content_type': ct.id, 'object_id': self.id})



    # This model rewrite the models.Model
class DiscussionModel(models.Model):
    discussions = GenericRelation(Discussion)

    class Meta:
        abstract = True

    def discussion_form(self):
        from .forms import AddDiscussionForm
        ct = ContentType.objects.get_for_model(self)

        return AddDiscussionForm(initial= {'content_type': ct.id,'object_id':self.id})




