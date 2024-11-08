from django.db import models


# новости и события
class News(models.Model):
    image = models.ImageField(upload_to='news/', verbose_name='загрузите фото')
    title = models.CharField(max_length=100, verbose_name='укажите название новости')
    description = models.TextField(verbose_name='Укажите написание новости')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


# Возможность менять лого фото
class LogoImage(models.Model):
    logo_image = models.ImageField(upload_to="logo_images", null=True, verbose_name='Загрузите фото лого')

    class Meta:
        verbose_name = 'фото лого'
        verbose_name_plural = 'фото логотипа'


# Таблица Почему выбирают нас

class Advanced(models.Model):
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Загрузите значок')
    text = models.TextField(null=True, verbose_name='Укажите почему выбирают вас')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'продвижение'
        verbose_name_plural = 'продвижения'


# WELCOME таблица

class Welcome(models.Model):
    description = models.TextField(verbose_name='дайте описания к ДОБРО ПОЖАЛОВАТЬ')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'добро пожаловать'
        verbose_name_plural = 'добро пожаловать'


# Таблица для обычных направлений
class Courses(models.Model):
    EXAM = (
        ('Да', 'Да'),
        ('Нет', 'Нет')
    )
    image = models.ImageField(upload_to='images/', null=True, verbose_name="Загрузите фото направления")
    course_name = models.CharField(max_length=100, null=True, verbose_name='Укажите название курса')
    description = models.TextField(verbose_name='укажите описания к курсу', null=True)
    some_information = models.TextField(verbose_name='укажите информацию о скидках', null=True)
    exam = models.CharField(max_length=100, verbose_name='есть ли вступительные экзамены', choices=EXAM, null=True)
    #lupic_ic = TextField
    #community = TextField


    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'направления'

class Mission(models.Model):
    mission = models.TextField(verbose_name='Напишите миссию института', default='')

    def __str__(self):
        return self.mission

    class Meta:
        verbose_name = 'миссия'
        verbose_name_plural = 'миссии'


# Таблица для IT направлений
class ITCourses(models.Model):
    EXAM = (
        ('Да', 'Да'),
        ('Нет', 'Нет')
    )
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Загрузите фото IT специальности')
    course_name = models.CharField(max_length=100, null=True, verbose_name='Укажите название курса')
    description = models.TextField(verbose_name='укажите описания к курсу', null=True)
    some_information = models.TextField(verbose_name='укажите информацию о скидках', null=True)
    exam = models.CharField(max_length=100, verbose_name='есть ли вступительные экзамены', choices=EXAM, null=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'IT направление'
        verbose_name_plural = 'IT направления'


# Таблица о нас контакты

class Contact(models.Model):
    street = models.CharField(max_length=100, verbose_name='Укажите улицу')
    number_1 = models.CharField(max_length=100, verbose_name='Укажите номер телефона 1')
    number_2 = models.CharField(max_length=100, verbose_name='Укажите номер телефона 2', blank=True)
    number_3 = models.CharField(max_length=100, verbose_name='Укажите номер телефона 3', blank=True)
    number_4 = models.CharField(max_length=100, verbose_name='Укажите номер телефона 4', blank=True)
    email = models.EmailField(verbose_name='Укажите EMAIL', default='@gmail.com')

    def __str__(self):
        return f'{self.street}-{self.number_1}'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
