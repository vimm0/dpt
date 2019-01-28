from django.contrib import admin

# Register your models here.
from apps.project.models import Project, Language, Category

projectFilter = ['id', 'modified']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Project._meta.fields if f.name not in projectFilter]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields if f.name != 'id']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Language._meta.fields if f.name != 'id']
