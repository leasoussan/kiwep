from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass



class TeamCommentsInlineAdmin(admin.TabularInline):
    pass

@admin.register(TeamCommentsBoard)
class TeamCommentAdmin(admin.ModelAdmin):
    pass
