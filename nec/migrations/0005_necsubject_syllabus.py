# Generated by Django 4.2.4 on 2023-10-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nec', '0004_chapter_necsubject_subject_code_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='necsubject',
            name='syllabus',
            field=models.ManyToManyField(blank=True, to='nec.chapter'),
        ),
    ]
