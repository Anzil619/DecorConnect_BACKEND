# Generated by Django 4.2.4 on 2023-09-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0012_remove_project_images_projectimages_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimages',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, to='professionals.projectimages'),
        ),
    ]
