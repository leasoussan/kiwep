from django.contrib import admin
from .models import Resource, Project, Mission, Team



@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("name", "field")
    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "field", "speaker", "completed")
    

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("name", "field")

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "group_Institution")
