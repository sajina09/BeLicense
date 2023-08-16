from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from license.db import TimeStampModel


# Create your models here.


class NECSubject(models.Model):
    subject_name = models.CharField(max_length=100, null=False, blank=False)
    syllabus = models.FileField(blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=["pdf"])])

    def __str__(self) :
     return self.subject_name



class Question(models.Model):
    subject = models.ForeignKey(NECSubject, models.RESTRICT, null=False, blank=False)
    title = RichTextField(null=False, blank=False)
    A = RichTextField(null=False, blank=False)
    B = RichTextField(null=False, blank=False)
    C = RichTextField(null=False, blank=False)
    D = RichTextField(null=False, blank=False)
    correct_answer = models.CharField(max_length=1, choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')), null=True, blank=True)
    explanation = RichTextField(null=False, default="N/A")
    group = models.CharField(max_length=1, choices=(('a', 'Group A'), ('b', 'Group B')), null=True, blank=True)

    def __str__(self) :
     return self.title



class ModelSet(models.Model):
    set_name = models.CharField(max_length=100, null=False, blank=False)
    questions = models.ManyToManyField(Question)

    def __str__(self) :
     return self.set_name