# Generated by Django 3.1 on 2022-09-08 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20220731_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='paper',
        ),
    ]