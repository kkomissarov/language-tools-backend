from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=50, unique=True)
    translate = models.CharField(max_length=50)
    context = models.TextField(blank=True, null=True)
