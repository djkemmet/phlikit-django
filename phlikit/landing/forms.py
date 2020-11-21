from django import forms
from .models import MailinglistSignUp

class MailinglistSignUpForm(forms.ModelForm):
    email_address = forms.EmailField()
    name = forms.CharField()


    class Meta:
        model = MailinglistSignUp
        fields = '__all__'