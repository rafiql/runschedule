# Generated by Django 3.0.3 on 2020-09-01 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='role',
        ),
    ]
