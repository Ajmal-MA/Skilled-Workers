from django.contrib import admin
from .models import SkillCategory, WorkerProfile, PreviousWork
# Register your models here.
@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(WorkerProfile)
class WorkerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'location', 'worker_type', 'bio_display')
    list_filter = ('worker_type',)   # ✅ replace skills with worker_type
    search_fields = ('user__username', 'phone', 'location')

    def bio_display(self, obj):
        return obj.bio[:30] + "..." if obj.bio else "-"
    bio_display.short_description = "Bio"
@admin.register(PreviousWork)
class PreviousWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'worker', 'completed_on')
    list_filter = ('completed_on', 'worker')
    search_fields = ('title', 'description', 'worker__user__username')


