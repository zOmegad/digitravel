# Generated by Django 4.1.4 on 2022-12-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0002_comment_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="body",
            field=models.TextField(max_length=200),
        ),
    ]
