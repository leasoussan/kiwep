from django.urls import reverse
from django.db import models
# from accounts.models import MyUser
from django.forms import modelform_factory
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext as _
from ckeditor.fields import RichTextField



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


    class Meta:
        ordering = ['date_posted']


    def __str__(self):
        return f'posted by: {self.user.username}'






class Discussion(Comment):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Discussions"

    def __str__(self):
        return f'discussion_title: {self.title}'

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







class Answer(DiscussionModel):
    STATUS_CHOICES =[
        ('w_r', _('waiting_review')),
        ('u_r',_('under_review')),
        ('a', _('accepted')),
        ('r', _('rejected')),
        ('c', _('see_comment')),
    ]
    response_comment = RichTextField(blank=True, null=True)
    response_file = models.FileField(null=True, blank=True)
    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default='w_r')
    date_posted = models.DateField(auto_now_add=True, blank=True, null=True)
    grade = models.IntegerField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        if self.content_type.model_class().__name__ == 'CollectiveMission':
            return f'answer by: {self.content_object.attributed_to}'
        else:
            return f'answer by: {self.content_object.attributed_to.user.first_name}'

    def status_form(self):
        from .forms import MissionSpeakerStatusAnswerForm
        return MissionSpeakerStatusAnswerForm(instance=self)


    def grade_form(self):
        from .forms import MissionSpeakerGradeAnswerForm
        return MissionSpeakerGradeAnswerForm(instance=self)


class AnswerModel(DiscussionModel):
    answer = GenericRelation(Answer)

    class Meta:
        abstract= True

    def answer_form(self):
        from .forms import AddAnswerForm
        ct = ContentType.objects.get_for_model(self)

        return AddAnswerForm(initial= {'content_type': ct.id, 'object_id':self.id})

