from django.db import models

class Goword(models.Model):
    slug = models.SlugField()
    url = models.CharField(max_length=512, blank=False, null=False)