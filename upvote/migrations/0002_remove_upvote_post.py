# Generated by Django 4.1.4 on 2022-12-15 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upvote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upvote',
            name='post',
        ),
    ]
