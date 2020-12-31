from django.db import models
from django.conf import settings

# Create your models here.
class ShortenedLink(models.Model):
    link = models.URLField()
    shortened_result = models.URLField()
    
    # https://stackoverflow.com/questions/7309588/django-foreign-key-to-user-model
    assigned_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.link

class LinkIntelligence(models.Model):
    link_visited = models.CharField(max_length=128)
    platform_on = models.CharField(max_length=128)
    visited_from = models.URLField()
    date_visited = models.DateTimeField()
        

    class Meta:
        verbose_name_plural = 'Click Data'

