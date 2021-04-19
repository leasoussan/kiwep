from django.contrib import admin
from .models import (
    Resource, 
    Project, 
    Mission, 
    Team,
    Skills,
    CollectiveProjectMission,
    IndividualProjectMission, 
)



# inline views
# class MissionsProjectInlineAdmin(admin.TabularInline):
#     model = MissionsProject

admin.site.register(IndividualProjectMission)
admin.site.register(CollectiveProjectMission)


class CollectiveProjectMissionInlineAdmin(admin.TabularInline):
    model = CollectiveProjectMission


# --------------------------------------------------------------------------


# model registration 

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("name", "field")
    


# --------------------------------------------------------------------------



class SkillsInlineAdmin(admin.TabularInline):
    model = Skills

admin.site.register(Skills)


# --------------------------------------------------------------------------



# --------------------------------------------------------------------------




@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "speaker", "completed")





# --------------------------------------------------------------------------


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("name", "field")


# --------------------------------------------------------------------------


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "group_Institution")
    # inlines =[CollectiveProjectMissionInlineAdmin]




# --------------------------------------------------------------------------