# Generated by Django 4.2.4 on 2023-09-17 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0002_firminfo_logo_alter_firminfo_awards_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firminfo',
            name='address',
        ),
        migrations.AddField(
            model_name='firminfo',
            name='address',
            field=models.ManyToManyField(to='professionals.address'),
        ),
    ]
