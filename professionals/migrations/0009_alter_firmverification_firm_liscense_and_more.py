# Generated by Django 4.2.4 on 2023-09-18 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professionals', '0008_alter_firminfo_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firmverification',
            name='firm_liscense',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='firmverification',
            name='gst_certificate',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='firmverification',
            name='insurance',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='firmverification',
            name='owner_pan_card',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
