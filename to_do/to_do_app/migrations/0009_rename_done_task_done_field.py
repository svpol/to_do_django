# Generated by Django 3.2.2 on 2022-01-28 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0008_auto_20220128_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='done',
            new_name='done_field',
        ),
    ]
