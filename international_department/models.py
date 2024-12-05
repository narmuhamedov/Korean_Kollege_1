from django.db import models


class EmployeeDepartment(models.Model):
    image = models.ImageField(upload_to="international_department_employee/")
    name = models.CharField(max_length=100, verbose_name="Укажите имя сотрудника")
    position = models.CharField(
        max_length=100, verbose_name="Укажите должность сотрудника"
    )
    email_employe = models.EmailField(verbose_name="укажите почту сотрудника")
    number = models.CharField(max_length=100, verbose_name="укажите номер телефона")
    address = models.CharField(max_length=100, verbose_name="укажите адрес")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "сотрудник"
        verbose_name_plural = "сотрудники"


class ShortStoryDepartment(models.Model):
    text = models.TextField(verbose_name="укажите краткую историю")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "краткую историю"
        verbose_name_plural = "краткая история"


class GeneralInformation(models.Model):
    text = models.TextField(verbose_name="укажите общую информацию")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "общую информацию"
        verbose_name_plural = "общая информация"


class DepartmentActivities(models.Model):
    text = models.TextField(verbose_name="укажите деятельность отдела")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "деятельность отдела"
        verbose_name_plural = "деятельности отдела"


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/")

    class Meta:
        verbose_name = "фотография"
        verbose_name_plural = "фотографии"


class RegulatoryDocuments(models.Model):
    name_document = models.CharField(
        max_length=150, verbose_name="укажите имя документа", null=True
    )
    url_document = models.URLField(verbose_name="вставьте ссылку на документ")

    def __str__(self):
        return self.url_document

    class Meta:
        verbose_name = "документ"
        verbose_name_plural = "документы"
