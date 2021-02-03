from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, CustomUserChangeForm
from .models import User, Student, Speaker, Institution

class CustomUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'username',]

admin.site.register(User, CustomUserAdmin)

admin.site.register(Student)

admin.site.register(Speaker)

admin.site.register(Institution)
