from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=300)
    entered_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title