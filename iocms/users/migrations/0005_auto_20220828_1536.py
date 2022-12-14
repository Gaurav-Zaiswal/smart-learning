# Generated by Django 3.1 on 2022-08-28 09:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_attendenceimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendenceimage',
            old_name='image',
            new_name='image1',
        ),
        migrations.CreateModel(
            name='RegisterVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='register_registration', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
