from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(CommentResponse)
class CommentResponseAdmin(admin.ModelAdmin):
    pass



class CommentsTeamInlineAdmin(admin.TabularInline):
    model = CommentsTeam

@admin.register(CommentsTeam)
class CommentsTeamAdmin(admin.ModelAdmin):
    pass


@admin.register(CommentsCollectiveMission)
class CommentsCollectiveMissionAdmin(admin.ModelAdmin):
    pass
