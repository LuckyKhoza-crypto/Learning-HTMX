# Generated by Django 5.0.3 on 2024-04-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='reserve',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
