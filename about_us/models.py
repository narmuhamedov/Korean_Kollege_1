from django.db import models

class About_Text(models.Model):
    text = models.TextField(verbose_name='укажите описание о колледже')

    def __str__(self):
        return self.text

