# Generated by Django 3.2.2 on 2022-01-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0010_alter_task_done_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done_field',
            field=models.BooleanField(default=False),
        ),
    ]
