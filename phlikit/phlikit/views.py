from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# So we can work with our shortened links.
from links.models import ShortenedLink

# Create your views here.


def handle_redirect(request, url_id):

    if request.method == 'GET':

        link_object = get_object_or_404(ShortenedLink, shortened_result=url_id )
        return redirect(link_object.link)