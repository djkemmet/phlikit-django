from django.db import models

# Create your models here.
class MailinglistSignUp(models.Model):
    email_address = models.EmailField(unique=True,max_length=254, help_text="Enter your email here.")
    name = models.CharField(max_length=254, help_text="What should we call you?")

    class Meta:
        verbose_name = 'Mailing List Entrie'

    def __str__(self):
        return self.email_address