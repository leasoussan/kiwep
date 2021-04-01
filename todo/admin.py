from django.contrib import admin
from .models import PersonalTask, TeamTask, Task

# Register your models here.

admin.site.register(Task)

admin.site.register(PersonalTask)
admin.site.register(TeamTask)