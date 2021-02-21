from django.contrib import admin
from .models import Field, Institution, InstitutionCategory, Level, Group


admin.site.register(Field)
admin.site.register(InstitutionCategory)
admin.site.register(Institution)

admin.site.register(Level)
admin.site.register(Group)
