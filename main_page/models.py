from django.db import models


# новости и события
class News(models.Model):
    image = models.ImageField(
        upload_to="news/", verbose_name="загрузите основное фото", null=True
    )
    image2 = models.ImageField(
        upload_to="news/", verbose_name="загрузите доп фото", null=True
    )
    image3 = models.ImageField(
        upload_to="news/", verbose_name="загрузите доп фото", null=True, blank=True
    )
    title = models.CharField(
        max_length=100, verbose_name="укажите название новости", null=True
    )
    description = models.TextField(verbose_name="Укажите написание новости")
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
        verbose_name = "новость"
        verbose_name_plural = "новости"


# Возможность менять лого фото
class LogoImage(models.Model):
    logo_image = models.ImageField(
        upload_to="logo_images", null=True, verbose_name="Загрузите фото лого"
    )

    class Meta:
        verbose_name = "фото лого"
        verbose_name_plural = "фото логотипа"


# Таблица Почему выбирают нас


class Advanced(models.Model):
    image = models.ImageField(
        upload_to="images/", null=True, verbose_name="Загрузите значок"
    )
    text = models.TextField(null=True, verbose_name="Укажите почему выбирают вас")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "продвижение"
        verbose_name_plural = "продвижения"


# WELCOME таблица


class Welcome(models.Model):
    description = models.TextField(verbose_name="дайте описания к ДОБРО ПОЖАЛОВАТЬ")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "добро пожаловать"
        verbose_name_plural = "добро пожаловать"


# Таблица для обычных направлений
class Courses(models.Model):
    image = models.ImageField(
        upload_to="images/", null=True, verbose_name="Загрузите фото направления"
    )
    course_name = models.CharField(
        max_length=100, null=True, verbose_name="Укажите название курса"
    )
    qualification = models.CharField(
        max_length=100, verbose_name="укажите квалификацию", null=True
    )
    description = models.TextField(verbose_name="укажите описания к курсу", null=True)
    year_study = models.CharField(
        max_length=100, verbose_name="укажите срок обучения", null=True
    )
    exam = models.CharField(
        max_length=100,
        verbose_name="есть ли вступительные экзамены",
        default='teasdasdasdxt',
        null=True,
    )
    lupic_ic = models.TextField(verbose_name='Укажите Lupic', null=True, blank=True)


    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = "направление"
        verbose_name_plural = "направления"


class Mission(models.Model):
    mission = models.TextField(verbose_name="Напишите миссию института", default="")

    def __str__(self):
        return self.mission

    class Meta:
        verbose_name = "миссия"
        verbose_name_plural = "миссии"


class OpenDoor(models.Model):
    open_door = models.TextField(verbose_name="укажите почему выбирают нас")

    def __str__(self):
        return self.open_door

    class Meta:
        verbose_name = "выбирают нас"
        verbose_name_plural = "выбрали нас"


# Таблица для IT направлений
class ITCourses(models.Model):
    image = models.ImageField(
        upload_to="images/", null=True, verbose_name="Загрузите фото IT специальности"
    )
    course_name = models.CharField(
        max_length=100, null=True, verbose_name="Укажите название курса"
    )
    description = models.TextField(verbose_name="укажите описания к курсу", null=True)
    qualification = models.CharField(
        max_length=100, verbose_name="укажите квалификацию", null=True
    )
    year_study = models.CharField(
        max_length=100, verbose_name="укажите срок обучения", null=True
    )
    exam = models.CharField(
        max_length=100,
        verbose_name="есть ли вступительные экзамены",
        default='texfsdfsdfsdft',
        null=True,
    )

    lupic_ic = models.TextField(verbose_name='Укажите Lupic', null=True, blank=True)

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = "IT направление"
        verbose_name_plural = "IT направления"


# Таблица о нас контакты


class Contact(models.Model):
    street = models.CharField(max_length=100, verbose_name="Укажите улицу")
    number_1 = models.CharField(max_length=100, verbose_name="Укажите номер телефона 1")
    number_2 = models.CharField(
        max_length=100, verbose_name="Укажите номер телефона 2", blank=True
    )
    number_3 = models.CharField(
        max_length=100, verbose_name="Укажите номер телефона 3", blank=True
    )
    number_4 = models.CharField(
        max_length=100, verbose_name="Укажите номер телефона 4", blank=True
    )
    email = models.EmailField(verbose_name="Укажите EMAIL", default="@gmail.com")

    def __str__(self):
        return f"{self.street}-{self.number_1}"

    class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"
