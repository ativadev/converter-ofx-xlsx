# Generated by Django 4.0.4 on 2022-05-09 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Uploaded',
            new_name='Upload',
        ),
    ]