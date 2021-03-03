from django.contrib import admin
from django.contrib.auth.admin import UserAdmin



from .forms import UserForm, MyUserCreationForm
from django.contrib.auth import get_user_model

from .models import MyUser, Student, Speaker, Representative, City, Country

class CustomUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = UserForm
    model = get_user_model
    list_display = ['id', 'email', 'username',]

admin.site.register(MyUser, CustomUserAdmin)

admin.site.register(Student)

admin.site.register(Speaker)
admin.site.register(Representative)


admin.site.register(City)
admin.site.register(Country)

