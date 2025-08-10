from django.contrib import admin
from . import models


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text"]


@admin.register(models.Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["question", "choice_text"]


@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["question", "choice"]