from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=256)
    category = models.ManyToManyField(Category)
    language = models.ManyToManyField(Language)
    location_local = models.CharField(max_length=256)
    git_remote_url = models.CharField(max_length=256)
    achivements = models.CharField(max_length=256)
    todo = models.CharField(max_length=256, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
