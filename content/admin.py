from django.contrib import admin
from .models import Resource, Project, Mission, Team, TeamProjectMission, Subjects,SkillsAcquired, RequiredSkills



# inline views
# class MissionsProjectInlineAdmin(admin.TabularInline):
#     model = MissionsProject

class TeamProjectMissionInlineAdmin(admin.TabularInline):
    model = TeamProjectMission


admin.site.register(TeamProjectMission)
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
    list_display = ("name", "field", "speaker", "completed")
    # inlines = [SkillsAcquiredInlineAdmin, RequiredSkillsInlineAdmin]





# --------------------------------------------------------------------------


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ("name", "field")


# --------------------------------------------------------------------------


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "group_Institution")
    inlines =[TeamProjectMissionInlineAdmin]




# --------------------------------------------------------------------------