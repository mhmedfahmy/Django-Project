# Generated by Django 2.0 on 2018-05-05 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180413_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AlterField(
            model_name='album',
            name='album_title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
