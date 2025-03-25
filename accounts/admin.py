from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import  CustomUserChangeForm
from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm   #when we apply this, an error occur
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields' : ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields' : ('age',)}),
    )



admin.site.register(CustomUser, CustomUserAdmin)

