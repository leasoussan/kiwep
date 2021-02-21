from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



from .forms import MyUserCreationForm, MyUserChangeForm
from django.contrib.auth import get_user_model

from .models import User, Student, Speaker, Representative, UserType, City, Country

class CustomUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = get_user_model
    list_display = ['email', 'username',]

admin.site.register(User, CustomUserAdmin)

admin.site.register(Student)

admin.site.register(Speaker)
admin.site.register(Representative)


admin.site.register(UserType)
admin.site.register(City)
admin.site.register(Country)

