from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass





@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    pass
