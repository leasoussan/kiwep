from django.contrib import admin
from message.admin import TeamCommentsInlineAdmin
from .models import (
    Resource, 
    Project, 
    Mission, 
    Team,
    Skills,
    CollectiveProjectMission,
    IndividualProjectMission, 
    IndividualCollectiveProjectMission,
    ProjectMissionRating, 
    ProjectMissionRating,
    HardSkillsRating
)



admin.site.register(ProjectMissionRating)
admin.site.register(HardSkillsRating)



class IndividualCollectiveProjectMissionInlineAdmin(admin.TabularInline):
    """ This Inline Tabular will show the form into a FK relation Admin View"""
    model = IndividualCollectiveProjectMission


class CollectiveProjectMissionInlineAdmin(admin.TabularInline):
    model = CollectiveProjectMission



class IndividualProjectMissionInlineAdmin(admin.TabularInline):
    model = IndividualProjectMission    


class ProjectMissionRatingInlineAdmin(admin.TabularInline):
    model = ProjectMissionRating    





class CollectiveProjectMissionAdmin(admin.ModelAdmin):
    """ Inlinve Admin view to show on other Admin Models"""
    inlines = [IndividualCollectiveProjectMissionInlineAdmin]
    


admin.site.register(IndividualProjectMission)
admin.site.register(CollectiveProjectMission, CollectiveProjectMissionAdmin)



class ProjectMissionRatingInlineAdmin(admin.TabularInline):
    model = ProjectMissionRating

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
    inlines = [ProjectMissionRatingInlineAdmin]




# --------------------------------------------------------------------------


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("name", "field")
    inlines = [ProjectMissionRatingInlineAdmin]


# --------------------------------------------------------------------------


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "group_Institution")
    inlines =[IndividualProjectMissionInlineAdmin, CollectiveProjectMissionInlineAdmin, TeamCommentsInlineAdmin]




# --------------------------------------------------------------------------