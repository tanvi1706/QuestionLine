from django.contrib import admin
from questions.models import Question, Answer
# Register your models here.

admin.site.register(Answer)
admin.site.register(Question)