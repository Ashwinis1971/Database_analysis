# Generated by Django 5.1 on 2024-09-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0004_placement_job_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=False, max_length=100, unique=True),
        ),
    ]