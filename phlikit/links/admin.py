from django.contrib import admin
from .models import ShortenedLink, LinkIntelligence
# Register your models here.

#
# Shortened Links
#

class ShortenedLinkAdmin(admin.ModelAdmin):
    list_display = ('assigned_user', 'shortened_result')
    #TODO: Change this so that the details of the shortened link come
    #      through for us to look at and see if we need to do anything. 

admin.site.register(ShortenedLink, ShortenedLinkAdmin)



#
#
#
class LinkIntelligenceAdmin(admin.ModelAdmin):
    list_display = ('link_visited',)

admin.site.register(LinkIntelligence, LinkIntelligenceAdmin)