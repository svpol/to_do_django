# Generated by Django 3.2.2 on 2022-01-28 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0009_rename_done_task_done_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done_field',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
