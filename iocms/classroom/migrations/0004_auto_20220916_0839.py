# Generated by Django 3.1 on 2022-09-16 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20220916_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroomstudents',
            name='classroom_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='classoom_relation', to='classroom.classroom'),
        ),
    ]