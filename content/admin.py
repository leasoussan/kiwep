from django.contrib import admin
from .models import (
    Resource, 
    Project, 
    Mission, 
    Team,
    Skills,
    CollectiveProjectMission,
    IndividualProjectMission, 
    IndividualCollectiveProjectMission,
    ProjectMissionRating
)




# inline views
# class MissionsProjectInlineAdmin(admin.TabularInline):
#     model = MissionsProject


class IndividualCollectiveProjectMissionInlineAdmin(admin.TabularInline):
    model = IndividualCollectiveProjectMission


class CollectiveProjectMissionAdmin(admin.ModelAdmin):
    inlines = [IndividualCollectiveProjectMissionInlineAdmin]
    

class CollectiveProjectMissionInlineAdmin(admin.TabularInline):
    model = CollectiveProjectMission
    

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


# --------------------------------------------------------------------------


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "group_Institution")
    # inlines =[CollectiveProjectMissionInlineAdmin]




# --------------------------------------------------------------------------