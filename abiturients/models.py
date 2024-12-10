from django.db import models

class AllQuestion(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Добавьте вопрос')
    answer_text = models.URLField(verbose_name='Вставьте ссылку на документ к вопросу из DRIVE')

    def __str__(self):
        return self.question_text


class EditionInformation(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='Добавьте вопрос')
    answer_text = models.URLField(verbose_name='Вставьте ссылку на документ к вопросу из DRIVE')

    def __str__(self):
        return self.question_text
