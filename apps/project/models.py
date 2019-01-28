from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)


class Language(models.Model):
    name = models.CharField(max_length=256)


class Project(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    location_local = models.CharField(max_length=256)
    git_remote_url = models.CharField(max_length=256)
    achivements = models.CharField(max_length=256)
    todo = models.CharField(max_length=256)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
