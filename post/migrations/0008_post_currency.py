# Generated by Django 4.1.4 on 2022-12-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_latitude_post_longitude_post_population'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='currency',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]