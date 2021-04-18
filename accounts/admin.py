from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from content.admin import  CollectiveProjectMissionInlineAdmin


from .forms import UserForm, MyUserCreationForm
from django.contrib.auth import get_user_model

from .models import MyUser, Student, Speaker, Representative, City, Country



class CustomUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = UserForm
    model = get_user_model
    list_display = ['id', 'email', 'username',]

    # def get_form(self, request, obj=None,**kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     is_superuser = request.user.is_superuser
    #     disable_fields = set()


    #     if not is_superuser:
    #         disable_fields |= {
    #             'username',
    #             'is_superuser',
    #             'user_permissions',
    #         }

    #     if (
    #         not is_superuser
    #         and obj is not None 
    #         and obj == request.user
    #     ):
    #         disable_fields |= {
    #             'is_staff',
    #             'is_superuser',
    #             'group',
    #             'user_permissions',
    #         }

    #     for f in disable_fields:
    #         if f in form.base_fields:
    #             form.base_fields[f].disabled = True

    #     return form

admin.site.register(MyUser, CustomUserAdmin)



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # inlines = [CollectiveProjectMissionInlineAdmin]
    pass

@admin.register(Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    pass


@admin.register(Representative)
class RepresentativeAdmin(admin.ModelAdmin):
    pass



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass