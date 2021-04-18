from django.contrib import admin
from .models import (
    Resource, 
    Project, 
    Mission, 
    Team, 
    Subjects,
    SkillsAcquired, 
    RequiredSkills,
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



class SubjectInlineAdmin(admin.TabularInline):
    model = Subjects

admin.site.register(Subjects)
# --------------------------------------------------------------------------


class SkillsAcquiredInlineAdmin(admin.TabularInline):
    model = SkillsAcquired

admin.site.register(SkillsAcquired)


# --------------------------------------------------------------------------


class RequiredSkillsInlineAdmin(admin.TabularInline):
    model = RequiredSkills

admin.site.register(RequiredSkills)


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