# Generated by Django 2.2 on 2020-02-28 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play_ground', '0006_remove_tweet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestant',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
