from django.contrib import admin
from message.admin import TeamCommentsInlineAdmin
from .models import (
    Resource,
    Project,
    Mission,
    Team,
    Skills,
    CollectiveMission,
    IndividualMission,
    MissionValue,
    HardSkillsRating, IndividualCollectiveMission
)



admin.site.register(MissionValue)
admin.site.register(HardSkillsRating)




class CollectiveMissionInlineAdmin(admin.TabularInline):
    model = CollectiveMission



class IndividualMissionInlineAdmin(admin.TabularInline):
    model = IndividualMission


class MissionValueInlineAdmin(admin.TabularInline):
    model = MissionValue



admin.site.register(IndividualCollectiveMission)




class ProjectMissionRatingInlineAdmin(admin.TabularInline):
    model = HardSkillsRating

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
    list_display = ("name", "speaker", "completed", "is_template")





# --------------------------------------------------------------------------


@admin.register(IndividualMission)
class IndividualMissionAdmin(admin.ModelAdmin):
    list_display = ("name", "field")



@admin.register(CollectiveMission)
class CollectiveMissionAdmin(admin.ModelAdmin):
    list_display = ("name", "field")



# --------------------------------------------------------------------------


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "group_Institution")




# --------------------------------------------------------------------------