# Generated by Django 4.2.4 on 2023-09-11 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeowners', '0003_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
