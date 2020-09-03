from django.db import models
from django.conf import settings
# Create your models here.

class Snippet(models.Model):
    snippet_title = models.CharField(max_length=100, null=True, blank=True)
    snippet_text = models.TextField(max_length=1500, null=False, blank=False)
    snippet_lang = models.CharField(max_length=100, null=False, blank=False)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
