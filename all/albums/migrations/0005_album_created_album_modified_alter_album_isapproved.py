# Generated by Django 4.1.6 on 2023-02-20 13:08

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_alter_album_managers_album_isapproved'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='album',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='album',
            name='isApproved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]