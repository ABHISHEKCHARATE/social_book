


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SocialUser

class SocialUserAdmin(UserAdmin):
    model = SocialUser
    list_display = ('email', 'username', 'full_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'city', 'state')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('full_name',  'city', 'state', 'location')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'full_name',  'city', 'state', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username', 'full_name')
    ordering = ('email',)

admin.site.register(SocialUser, SocialUserAdmin)
