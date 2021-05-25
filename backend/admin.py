from django.contrib import admin
from .models import Field, Institution, InstitutionCategory, Group, Level



@admin.register(Level)
class FieldAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass




@admin.register(InstitutionCategory)
class InstitutionCategoryAdmin(admin.ModelAdmin):
    pass





@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass