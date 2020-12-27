from django.contrib import admin
from .models import ShortenedLink
# Register your models here.

#
# Shortened Links
#

class ShortenedLinkAdmin(admin.ModelAdmin):
    list_display = ('assigned_user','link','shortened_result')
    

admin.site.register(ShortenedLink, ShortenedLinkAdmin)