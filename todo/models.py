from django.db import models
from django.contrib.dispatch import receiver
from django.db.models.signals import post_save


class Task(models.Model):
    title = models.CharField(max_length=300)
    details = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    creator = models.ForeignKey('accounts.MyUser', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title



class PersonalTask(Task):
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title



class TeamTask(Task):
    team = models.ForeignKey('content.Team', on_delete=models.CASCADE)
    assignees = models.ManyToManyField('accounts.Student', through= "StudentTeamTask", blank=True)
    def __str__(self):
        return f'{self.title} of {self.user.first_name}'


# here we want to listen to a pres save to know what to do- use the signal




class AssignedTask(Task):
    assignee = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    completed = models.BooleanField(default=Fals)
    
    def __str__(self):
        return self.assignee

   


class StudentTeamTask(models.Model):
    team_task = models.ForeignKey(TeamTask, on_delete=models.CASCADE)
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} of {self.team.name}'

@receiver(post_save, sender=TeamTask)
def save_to_assignees(sender, created, instance, **kwargs):
    if created:
        students = [StudentTeamTask(team_task=instance, student=student) for student in instance.team.participants.all() ]
        StudentTeamTask.objects.bulk_create(students)




    # class Meta:
    #     abstract =False
    # # this doenst allows me to query on the taks 
# we ll do abstact Model 
# we are not goint to make a table for this class only to inherit - we wont have a task table
