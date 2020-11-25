from django import forms
from .models import MailinglistSignUp

class MailinglistSignUpForm(forms.ModelForm):
    email_address = forms.EmailField(label="Email", initial="Enter your email.")
    name = forms.CharField(label="Name", initial="What should we call you?")


    class Meta:
        model = MailinglistSignUp
        fields = '__all__'