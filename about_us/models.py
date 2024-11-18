from django.db import models

class About_Text(models.Model):
    text = models.TextField(verbose_name='укажите описание о колледже')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'описание о вузе'
        verbose_name_plural = 'описания о вузе'


class About_AUP(models.Model):
    image = models.ImageField(upload_to='aup/', verbose_name='загрузите фото')
    position = models.CharField(max_length=100, verbose_name='укажите должность')
    name = models.CharField(max_length=100, verbose_name='укажите инициалы')
    description = models.TextField(verbose_name='укажите информацию о человеке')
    education = models.TextField(verbose_name='укажите образование', null=True)
    qualification = models.TextField(verbose_name='укажите повышение квалификации', null=True)
    achievements = models.TextField(verbose_name='какие достижения вы достигли', null=True)
    sertificate_url = models.URLField(verbose_name='укажите ссылку на свой сертификат из DRIVE', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'должность AUP'
        verbose_name_plural = 'должности AUP'


class About_PPC(models.Model):
    image = models.ImageField(upload_to='ppc/', verbose_name='загрузите фото преподавателя')
    name = models.CharField(max_length=100, verbose_name='укажите инициалы преподавателя')
    course = models.CharField(max_length=100, verbose_name='Укажите какие курсы он преподает')
    description = models.TextField(verbose_name='укажите информацию о преподавателе')
    education = models.TextField(verbose_name='укажите образование', null=True)
    qualification = models.TextField(verbose_name='укажите повышение квалификации', null=True)
    achievements = models.TextField(verbose_name='какие достижения вы достигли', null=True)
    sertificate_url = models.URLField(verbose_name='укажите ссылку на свой сертификат из DRIVE', null=True)


    def __str__(self):
        return f'{self.name} {self.course}'

    class Meta:
        verbose_name = 'преподаватель'
        verbose_name_plural = 'преподаватели'
