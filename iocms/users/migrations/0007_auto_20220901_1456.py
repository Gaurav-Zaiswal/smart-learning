# Generated by Django 3.1 on 2022-09-01 09:11

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20220828_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registervideo',
            name='video',
            field=models.FileField(upload_to=users.models.register_video_path),
        ),
    ]
