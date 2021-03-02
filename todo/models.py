from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=300)
    entered_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False, blank=True, null=True)
    team_task = models.ForeignKey('content.Team', on_delete=models.CASCADE, null=True, related_name='tasks')

    def __str__(self):
        return self.title