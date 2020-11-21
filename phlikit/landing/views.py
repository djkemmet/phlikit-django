from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MailinglistSignUpForm

# Create your views here.
def index(request):
    form = MailinglistSignUpForm()
    return render(request, 'landing/landing_page.html', {'form': form})

def update_MailinglistSignUp(request):

#
# This only provides a POST endpoint to add emails to our Mailing List DB
#

    form = MailinglistSignUpForm()

    if request.method == 'POST':
        form = MailinglistSignUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        
            return redirect('/signup/')
        else:
            print(form.errors)