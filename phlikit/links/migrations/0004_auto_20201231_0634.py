# Generated by Django 3.1.2 on 2020-12-31 06:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_linkintelligence'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='linkintelligence',
            options={'verbose_name_plural': 'Click Data'},
        ),
        migrations.AddField(
            model_name='linkintelligence',
            name='date_visited',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 31, 6, 34, 50, 554616, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
