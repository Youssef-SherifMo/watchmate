# Generated by Django 4.1 on 2022-08-07 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='describition',
            new_name='description',
        ),
    ]
