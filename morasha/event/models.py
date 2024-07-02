from django.db import models

class Answers(models.Model):
    user = models.TextField(verbose_name="Пользователь")
    question_name = models.TextField(verbose_name="Номер вопроса")
    answer = models.TextField(verbose_name="Ответ на вопрос")
    sort_id = models.IntegerField(verbose_name="id for sort")


    class Meta:
        verbose_name = "Вопрос-ответ"
        verbose_name_plural = "Вопросы-ответы"

    def __str__(self):
        return f"{self.question_name}, ответ от {self.user}"


class Questions(models.Model):
    link_id = models.IntegerField(verbose_name="ID ссылки")
    question_name = models.TextField(verbose_name="Номер вопроса")
    question = models.TextField(verbose_name="Вопрос")

    class Meta:
        verbose_name = "Вопрос для ивента"
        verbose_name_plural = "Вопросы для ивента"

    def __str__(self):
        return f"{self.question_name}"
    

class EventUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField(verbose_name="Имя", unique=True)

    def __str__(self):
        return f"id_{self.user_id} - {self.user_name}"