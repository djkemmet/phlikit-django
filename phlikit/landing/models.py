from django.db import models

# Create your models here.
class MailinglistSignUp(models.Model):
    email_address = models.EmailField(unique=True,max_length=254)
    name = models.CharField(max_length=254)
    zipcode = models.CharField(max_length=5)
    uses_facebook = models.BooleanField(default=False)
    uses_twitter = models.BooleanField(default=False)
    uses_instagram = models.BooleanField(default=False)
    uses_parler = models.BooleanField(default=False)
    uses_lbry = models.BooleanField(default=False)
    


    class Meta:
        verbose_name = 'Mailing List Entrie'

    def __str__(self):
        return self.email_address