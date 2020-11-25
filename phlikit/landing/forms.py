from django import forms
from .models import MailinglistSignUp

class MailinglistSignUpForm(forms.ModelForm):
    email_address = forms.EmailField(label="Email", initial="Enter your email.")
    name = forms.CharField(label="Name", initial="What should we call you?")
    zipcode = forms.CharField(label="Zip Code",  initial="What's your Zipcode?")
    uses_facebook = forms.BooleanField(label="Facebook", required=False)
    uses_twitter = forms.BooleanField(label="Twitter", required=False)
    uses_instagram = forms.BooleanField(label="Instagram", required=False)    
    uses_parler = forms.BooleanField(label="Parler", required=False)
    uses_lbry = forms.BooleanField(label="lbry", required=False)


    class Meta:
        model = MailinglistSignUp
        fields = '__all__'