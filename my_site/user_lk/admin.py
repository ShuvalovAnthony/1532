from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'phone',
        'course',
    ]
    list_display_links = ('user',)
    search_fields = ('user', )


admin.site.register(Profile, ProfileAdmin)
