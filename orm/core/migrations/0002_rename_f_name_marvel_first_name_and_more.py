# Generated by Django 5.1.1 on 2025-02-07 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marvel',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='marvel',
            old_name='l_name',
            new_name='last_name',
        ),
    ]
