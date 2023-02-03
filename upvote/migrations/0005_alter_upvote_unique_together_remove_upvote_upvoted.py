# Generated by Django 4.1.4 on 2022-12-20 14:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("review", "0003_alter_review_unique_together"),
        ("upvote", "0004_upvote_review"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="upvote",
            unique_together={("user", "review")},
        ),
        migrations.RemoveField(
            model_name="upvote",
            name="upvoted",
        ),
    ]
