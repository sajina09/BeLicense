from django.contrib import admin
from nec.models import NECSubject, Question, ModelSet
# Register your models here.


class NECSubjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(NECSubject, NECSubjectAdmin)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
