# Generated by Django 3.2.2 on 2022-01-24 08:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date(2022, 1, 24)),
        ),
    ]
