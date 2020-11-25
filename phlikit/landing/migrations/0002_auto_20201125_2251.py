# Generated by Django 3.1.2 on 2020-11-25 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailinglistsignup',
            options={'verbose_name': 'Mailing List Entrie'},
        ),
        migrations.AddField(
            model_name='mailinglistsignup',
            name='uses_facebook',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mailinglistsignup',
            name='uses_instagram',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mailinglistsignup',
            name='uses_lbry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mailinglistsignup',
            name='uses_parler',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mailinglistsignup',
            name='uses_twitter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mailinglistsignup',
            name='zipcode',
            field=models.CharField(default=11111, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mailinglistsignup',
            name='email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='mailinglistsignup',
            name='name',
            field=models.CharField(max_length=254),
        ),
    ]
