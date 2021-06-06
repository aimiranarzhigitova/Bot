from django.db import models


class Profile(models.Model):
    extenal_id = models.PositiveIntegerField("ID user", unique=True)
    name = models.TextField("User name")

    def __str__(self):
        return f'{self.extenal_id}{self.name}'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):
    profile = models.ForeignKey(
        to="bot.Profile",
        verbose_name="Профиль",
        on_delete=models.CASCADE,
    )

    text = models.TextField(
        'Текст',
    )
    created_at = models.DateTimeField(
        "Время получение",
        auto_now_add=True,
    )

    def __str__(self):
        return f"Сообщение  {self.pk} от {self.profile}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"