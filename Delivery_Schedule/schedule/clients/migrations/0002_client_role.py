# Generated by Django 3.0.3 on 2020-08-24 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='role',
            field=models.CharField(default='User', max_length=256),
        ),
    ]
