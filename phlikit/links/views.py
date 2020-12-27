from django.shortcuts import render, redirect
from django.http import HttpResponse
from links import forms
from links.models import ShortenedLink
from Resources import helpers

def root(request):
    return redirect('/home/')


# Create your views here.
def shorten(request):
    
    # Define which form we're reciving
    form = forms.LinkShorteningForm()


    # What should we do if we're RECIEVING a link to shorten?
    if request.method == 'POST':

        # First, make a local variable from the FORM recieved from the POST REQUEST
        form = forms.LinkShorteningForm(request.POST)

        # If the form to shorten a link checks out...
        if form.is_valid():
            view_context = {}
            
            # Create a new instances of a shortenedLink model
            shortend_link = ShortenedLink()
            
            # Set It's relevant properties
            shortend_link.link = request.POST['link']
            shortend_link.shortened_result = helpers.generate_link_id()
            shortend_link.assigned_user = request.user
            
            # Save the new model to our database
            shortend_link.save()
            view_context['shortened_link'] = 'https://poztd.it/l/' + shortend_link.shortened_result

            # Return to the user with a view that contains the
            # now shortened link.
            return render(request, 'links/shortened_link_result.html', context=view_context)

            #unpack the request to get the link 
            return redirect('/home/')


    if request.method == 'GET':
        
        shortend_data = {}
        shortend_data['form'] = forms.LinkShorteningForm

        return render(request, 'links/shorten_link.html', context=shortend_data)



