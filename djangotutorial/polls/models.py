from django.db import models
from django.utils import timezone
from django.conf import settings


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)


    class Meta:
        permissions = [
            ("can_answer_question", "Can answer question")
        ]

    def __str__(self):
        return self.question_text if len(self.question_text) < 15 else f"{self.question_text[:15]}..."


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'order'], name='unique question and order')
        ]


    def __str__(self):
        return self.choice_text if len(self.choice_text) < 15 else f"{self.choice_text[:15]}..."


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['question', 'choice', 'user'], name='unique question and choice')
        ]


    def __str__(self):
        return f'{self.question}: {self.choice}'
