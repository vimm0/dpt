from django.contrib import admin

# Register your models here.
from apps.project.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Project._meta.fields if f.name != 'id']
