# Generated by Django 4.2.4 on 2023-09-16 18:17

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NECSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_link', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor.fields.RichTextField()),
                ('A', ckeditor.fields.RichTextField()),
                ('B', ckeditor.fields.RichTextField()),
                ('C', ckeditor.fields.RichTextField()),
                ('D', ckeditor.fields.RichTextField()),
                ('correct_answer', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, null=True)),
                ('explanation', ckeditor.fields.RichTextField(default='N/A')),
                ('group', models.CharField(choices=[('a', 'Group A'), ('b', 'Group B')], max_length=1, verbose_name='Question Group')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='nec.necsubject')),
            ],
        ),
        migrations.CreateModel(
            name='ModelSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=100)),
                ('model_set_link', models.CharField(default='', max_length=100)),
                ('questions', models.ManyToManyField(to='nec.question')),
                ('subject', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='nec.necsubject')),
            ],
        ),
    ]
