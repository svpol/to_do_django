# Generated by Django 3.2.2 on 2022-01-31 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0012_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.date(2022, 1, 31)),
        ),
    ]
