from django.db import models

class StudentLive(models.Model):
    image = models.ImageField(
        upload_to="student_live/", verbose_name="загрузите основное фото", null=True
    )
    image2 = models.ImageField(
        upload_to="student_live2/", verbose_name="загрузите доп фото", null=True
    )
    image3 = models.ImageField(
        upload_to="student_live3/", verbose_name="загрузите доп фото", null=True, blank=True
    )
    title = models.CharField(
        max_length=100, verbose_name="укажите название мероприятия", null=True
    )
    description = models.TextField(verbose_name="Укажите описание мероприятия")
    video_url = models.URLField(
        verbose_name="укажите ссылку с youtube", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров", null=True
    )  # Поле просмотров

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "мероприятие"
        verbose_name_plural = "мероприятия"