# Generated by Django 2.0.5 on 2019-07-14 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageapp', '0002_auto_20190714_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]