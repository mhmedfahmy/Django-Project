# Generated by Django 2.0 on 2018-05-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='is_favorite',
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(upload_to=''),
        ),
    ]
