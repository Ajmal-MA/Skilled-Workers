from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')   # use "role"
    list_filter = ('role',)           # use "role"
    search_fields = ('user__username',)
