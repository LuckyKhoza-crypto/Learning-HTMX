# Generated by Django 5.0.3 on 2024-04-03 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_event_reserve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='reserve',
        ),
    ]