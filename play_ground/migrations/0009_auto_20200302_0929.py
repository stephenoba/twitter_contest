# Generated by Django 2.2 on 2020-03-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play_ground', '0008_remove_contestant_track'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweet',
            field=models.CharField(max_length=200),
        ),
    ]