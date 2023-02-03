# Generated by Django 4.1.4 on 2022-12-20 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0003_alter_review_unique_together"),
        ("upvote", "0003_alter_upvote_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="upvote",
            name="review",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="review.review",
            ),
            preserve_default=False,
        ),
    ]
