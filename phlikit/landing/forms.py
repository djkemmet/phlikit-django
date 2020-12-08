from django import forms
from .models import MailinglistSignUp

class MailinglistSignUpForm(forms.ModelForm):
    email_address = forms.EmailField(label="Email", widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Email'}),
                            required=True)
    name = forms.CharField(label="Name", widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'How we should refer to you'}),
                            required=True)
    zipcode = forms.CharField(label="Zip Code",  widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Zipcode'}),
                            required=True)
    uses_facebook = forms.BooleanField(label="Facebook", required=False)
    uses_twitter = forms.BooleanField(label="Twitter", required=False)
    uses_instagram = forms.BooleanField(label="Instagram", required=False) 
    uses_youtube = forms.BooleanField(label="Youtube", required=False)
    uses_parler = forms.BooleanField(label="Parler", required=False)
    uses_lbry = forms.BooleanField(label="lbry", required=False)


    class Meta:
        model = MailinglistSignUp
        fields = '__all__'