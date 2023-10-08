from django.contrib import admin
from django.db import models
from django import forms
from nec.models import NECSubject, Question, ModelSet, Chapter, Topic


# Register your models here.


class NECSubjectAdmin(admin.ModelAdmin):
    search_fields = ['subject_name']
    filter_horizontal = ('syllabus',)
    # list_filter = ['subject']


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
    fields = ["set_name", "model_set_link", "subject", "questions"]
    # def render_change_form(
    #     self, request, context, add=False, change=False, form_url="", obj=None
    # ):
    #     context["adminform"].form.fields["questions"].queryset = Question.objects.filter(
    #         subject=context["adminform"].form.instance.subject)
    #     return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)
    #
    # def get_form(self, request, obj=None, change=False, **kwargs):
    #     return super().get_form(request, obj, change, **kwargs)


class ChapterListAdmin(admin.TabularInline):
    model = Chapter
    extra = 2
    verbose_name = "Sub-chapter"
    verbose_name_plural = "Sub-chapters"
    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={'size': '50'})
        }
    }


class TopicListAdmin(admin.TabularInline):
    model = Topic
    extra = 2
    verbose_name = "Topic"
    verbose_name_plural = "Topics"
    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={'size': '100'})
        }
    }


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    inlines = [ChapterListAdmin, TopicListAdmin]
    fields = ["chapter_name", "chapter_code", "parent_chapter"]
    list_filter = ["chapter_name"]
    search_fields = ["chapter_name", "chapter_code"]
    search_help_text = "Type chapter name or chapter code"
    autocomplete_fields = ['parent_chapter']
    formfield_overrides = {
        models.CharField: {
            'widget': forms.TextInput(attrs={'size': '100'})
        }
    }

    def get_inlines(self, request, obj):
        return self.inlines[1:] if obj and obj.parent_chapter else self.inlines[:1]

    def get_fields(self, request, obj=None):
        return self.fields if obj and obj.parent_chapter else self.fields[:-1]


class SubChapterList(admin.SimpleListFilter):
    parameter_name = "chapter"
    title = "Sub chapter"

    def queryset(self, request, queryset):
        # print(next(choice[0] for choice in self.lookup_choices if choice[1]==self.value()))
        if val := self.value():
            return queryset.filter(chapter__id=self.value())
        return queryset

    def lookups(self, request, model_admin):
        return list(Chapter.objects.filter(parent_chapter__isnull=False).values_list("id", "chapter_name"))


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'topic_name']
    autocomplete_fields = ['chapter']
    list_filter = (SubChapterList,)

    def get_form(self, request, obj=None, **kwargs):
        form = super(TopicAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['chapter'].queryset = Chapter.objects.filter(
            parent_chapter__isnull=False)
        return form
