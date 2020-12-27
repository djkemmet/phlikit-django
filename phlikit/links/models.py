from django.db import models
from django.conf import settings

# Create your models here.
class ShortenedLink(models.Model):
    link = models.URLField()
    shortened_result = models.URLField(unique=True)

    # https://stackoverflow.com/questions/7309588/django-foreign-key-to-user-model
    assigned_user = models.IntegerField(unique=False)
