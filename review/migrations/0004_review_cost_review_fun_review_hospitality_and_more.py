# Generated by Django 4.1.4 on 2022-12-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0003_alter_review_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="cost",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="review",
            name="fun",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="review",
            name="hospitality",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="review",
            name="internet",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="review",
            name="life_quality",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="review",
            name="safety",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="review",
            name="score",
            field=models.FloatField(),
        ),
    ]
