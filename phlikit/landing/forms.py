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
    PArtner = forms.CharField(label="Would you like to be a tester?",  widget=forms.Select({
                                   'class': 'form-control',
                                   'placeholder': 'Explain here.'}),
                            required=True)
    Media = forms.CharField(label="What do you use your platforms for?",  widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Explain here.'}),
                            required=True)
    Feastures = forms.CharField(label="Are there any features you would like to see?",  widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'List here.'}),
                            required=True)
    comment = forms.CharField(label="If you have any questions or comments, please enter them below?",  widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': 'Comment here.'}),
                            required=True)

    class Form(forms.Form):
       field = forms.TypedChoiceField(coerce=lambda x: x =='True', 
                                   choices=((False, 'No'), (True, 'Yes')))


    class Meta:
        model = MailinglistSignUp
        fields = '__all__'