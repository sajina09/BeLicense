from django.contrib import admin
from nec.models import NECSubject, Question, ModelSet
# Register your models here.


class NECSubjectAdmin(admin.ModelAdmin):
    search_fields = ['subject_name']


admin.site.register(NECSubject, NECSubjectAdmin)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['subject', 'group']


@admin.register(ModelSet)
class ModelSetAdmin(admin.ModelAdmin):
    search_fields = ['set_name']
    filter_horizontal = ('questions',)
    list_filter = ['subject']

