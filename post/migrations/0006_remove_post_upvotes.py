# Generated by Django 4.1.4 on 2022-12-20 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_upvotes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upvotes',
        ),
    ]
