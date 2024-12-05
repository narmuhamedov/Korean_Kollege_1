from django.db import models


# Create your models here.
class License(models.Model):
    name_doc = models.CharField(
        max_length=100, verbose_name="укажите название документа", null=True
    )
    url_doc = models.URLField(
        verbose_name="Укажите путь из DRIVE для лицензии", null=True
    )

    def __str__(self):
        return self.name_doc

    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"


class Normative_legal_acts(models.Model):
    name_doc = models.CharField(
        max_length=100, verbose_name="укажите название документа"
    )

    def __str__(self):
        return self.name_doc

    class Meta:
        verbose_name = "Нормативно правовой акт"
        verbose_name_plural = "Нормативно правовые акты"


class Category_acts(models.Model):
    category_model = models.ForeignKey(
        Normative_legal_acts,
        on_delete=models.CASCADE,
        related_name="category_acts",
        verbose_name="выберите категорию",
    )
    name_doc_act = models.CharField(
        max_length=100, verbose_name="укажите название документа"
    )
    url_doc = models.URLField(
        verbose_name="Укажите путь из DRIVE из нужного акта", null=True
    )

    def __str__(self):
        return f"{self.name_doc_act} - {self.category_model}"

    class Meta:
        verbose_name = "Категорию актов"
        verbose_name_plural = "Категории актов"


class Organizational_structure(models.Model):
    name_doc = models.CharField(
        max_length=100, verbose_name="укажите название документа"
    )
    url_doc = models.URLField(
        verbose_name="Укажите путь из DRIVE для Организационной структуры", null=True
    )

    def __str__(self):
        return self.name_doc

    class Meta:
        verbose_name = "организационная структура"
        verbose_name_plural = "организационные структуры"
