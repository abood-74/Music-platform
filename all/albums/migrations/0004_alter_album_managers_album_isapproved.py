# Generated by Django 4.0.7 on 2023-02-19 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_alter_album_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='album',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='isApproved',
            field=models.BooleanField(default=False),
        ),
    ]