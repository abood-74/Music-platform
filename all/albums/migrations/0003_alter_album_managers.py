# Generated by Django 4.0.7 on 2023-02-19 22:40

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_artist'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='album',
            managers=[
                ('track', django.db.models.manager.Manager()),
            ],
        ),
    ]
