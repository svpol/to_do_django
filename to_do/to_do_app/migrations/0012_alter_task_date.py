# Generated by Django 3.2.2 on 2022-01-31 12:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0011_alter_task_done_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 31, 12, 35, 14, 597995, tzinfo=utc)),
        ),
    ]
