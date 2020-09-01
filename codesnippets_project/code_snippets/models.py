from django.db import models
from users.models import User
# Create your models here.

class Snippet(models.Model):
    snippet_text = models.CharField(max_length=255, null=False, blank=False)
    user = models.ManyToManyField(User)