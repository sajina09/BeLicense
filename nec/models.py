from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.


class NECSubject(models.Model):
    subject_name = models.CharField(max_length=100, null=False, blank=False)
    # syllabus = models.FileField(blank=True, null=True, validators=[
    #                             FileExtensionValidator(allowed_extensions=["pdf"])])
    subject_link = models.CharField(
        max_length=100, null=False, blank=False, default='')
    picture_link = models.CharField(
        max_length=100, null=False, blank=False, default='')

    class Meta:
        ordering = ["subject_name"]

    def __str__(self):
        return self.subject_name


class Question(models.Model):
    subject = models.ForeignKey(
        NECSubject, models.RESTRICT, null=False, blank=False)
    title = RichTextField(null=False, blank=False)
    A = RichTextField(null=False, blank=False)
    B = RichTextField(null=False, blank=False)
    C = RichTextField(null=False, blank=False)
    D = RichTextField(null=False, blank=False)
    correct_answer = models.CharField(max_length=1, choices=(
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'None')), null=True, blank=True)
    explanation = RichTextField(null=False, default="N/A",)
    group = models.CharField(max_length=1, choices=(
        ('a', 'Group A'), ('b', 'Group B')), null=False, blank=False, verbose_name='Question Group')

    def __str__(self):
        return self.title


class ModelSet(models.Model):
    set_name = models.CharField(max_length=100, null=False, blank=False)
    questions = models.ManyToManyField(Question)
    model_set_link = models.CharField(
        max_length=100, null=False, blank=False, default='')
    subject = models.ForeignKey(
        NECSubject, on_delete=models.CASCADE, null=True, blank=True, default=None)
    # slug = models.SlugField(unique=False, blank=True)

    # def save(self, *args, **kwargs):
    #     # Automatically generate the slug from the set_name field
    #     self.slug = slugify(self.set_name)
    #     super(ModelSet, self).save(*args, **kwargs)
    class Meta:
        ordering = ["set_name"]

    def __str__(self):
        return self.set_name
