# Generated by Django 4.2.4 on 2023-09-19 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0011_firminfo_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='images',
        ),
        migrations.AddField(
            model_name='projectimages',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='professionals.project'),
            preserve_default=False,
        ),
    ]