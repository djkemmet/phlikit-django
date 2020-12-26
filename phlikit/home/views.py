from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def user_home(request):
    user_home_data = {}

    # user is signed in, let them do stuff.
    if request.user.is_authenticated:
        return render(request, 'home/user_home.html', context=user_home_data)
    
    # Send them home, they're not logged in they don't need to see anything here. 
    else:
        return redirect('/')