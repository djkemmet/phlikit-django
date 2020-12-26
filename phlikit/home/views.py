from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def user_home(request):

    # user is signed in, let them do stuff.
    if request.user.is_authenticated:
        return HttpResponse('<h1> The user has signed in and been directed to their home page</h1>')
    
    # Send them home, they're not logged in they don't need to see anything here. 
    else:
        return redirect('/')