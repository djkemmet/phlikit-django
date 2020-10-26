from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import MailinglistSignUpForm

# Create your views here.
def index(request):
    return render(request, 'landing/landing_page.html')

def update_MailinglistSignUp(request):

    form = MailinglistSignUpForm()

    if request.method == 'POST':
        form = MailinglistSignUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        
            return redirect('/signup/')
        else:
            print(form.errors)

    return render(request, 'landing/MailinglistSignUpForm.html', {'form': form})