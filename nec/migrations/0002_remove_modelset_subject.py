# Generated by Django 4.2.4 on 2023-09-03 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nec', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelset',
            name='subject',
        ),
    ]
