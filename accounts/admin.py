from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from content.admin import  CollectiveMissionInlineAdmin


from .forms import UserForm, MyUserCreationForm
from django.contrib.auth import get_user_model

from .models import MyUser, Student, Speaker, Representative, City, Country


#
# class CustomUserAdmin(UserAdmin):
#     """ Basic User """
#     add_form = MyUserCreationForm
#     form = UserForm
#
#     model = get_user_model()
#     list_display = ['id', 'email', 'username',]

# admin.site.register(MyUser, CustomUserAdmin)



class CustomUserAdmin(UserAdmin):
    model = MyUserCreationForm

    search_fields = ('email',)
    ordering = ('email',)

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


