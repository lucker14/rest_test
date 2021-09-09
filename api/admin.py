from django.contrib import admin

from .models import Task


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("label", "completed", "relates_to")


admin.site.register(Task, TaskAdmin)
