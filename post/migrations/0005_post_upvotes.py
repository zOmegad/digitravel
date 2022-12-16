# Generated by Django 4.1.4 on 2022-12-15 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upvote', '0002_remove_upvote_post'),
        ('post', '0004_remove_post_upvote_remove_post_upvoted_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upvotes',
            field=models.ManyToManyField(related_name='upvotes', to='upvote.upvote'),
        ),
    ]