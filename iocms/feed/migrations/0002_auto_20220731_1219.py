# Generated by Django 3.1 on 2022-07-31 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroomfeed',
            name='posted_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher'),
        ),
        migrations.AddConstraint(
            model_name='classroomfeed',
            constraint=models.CheckConstraint(check=models.Q(('assignment_id__isnull', False), ('feed_description__isnull', False), _connector='OR'), name='both_not_null'),
        ),
    ]
