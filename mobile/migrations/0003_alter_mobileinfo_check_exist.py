# Generated by Django 5.1.2 on 2024-11-01 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_mobileinfo_delete_moblieinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileinfo',
            name='check_exist',
            field=models.IntegerField(choices=[(0, '-'), (1, '+')], default=1),
        ),
    ]
