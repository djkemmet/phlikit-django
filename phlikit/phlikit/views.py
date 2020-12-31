from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from datetime import datetime

# So we can work with our shortened links.
from links.models import ShortenedLink, LinkIntelligence

# Create your views here.


def handle_redirect(request, url_id):

    if request.method == 'GET':


        link_object = get_object_or_404(ShortenedLink, shortened_result=url_id )
        
        Instance_of_link_intelligence = LinkIntelligence()
        
        Instance_of_link_intelligence.link_visited = url_id
        Instance_of_link_intelligence.platform_on = request.META['HTTP_USER_AGENT']
        Instance_of_link_intelligence.visited_from = request.META['REMOTE_ADDR']
        Instance_of_link_intelligence.date_visited = datetime.now().strftime('%Y-%m-%d %I:%M')



        # Save this data to the database.
        Instance_of_link_intelligence.save()


        return redirect(link_object.link)