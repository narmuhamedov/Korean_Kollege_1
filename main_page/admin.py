from django.utils.html import format_html
from django.contrib import admin
from . import models
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from PIL import Image

class ImageForm(ModelForm):
    class Meta:
        model = models.LogoImage
        fields = ("logo_image",)

    def clean(self):
        super().clean()
        if self.cleaned_data.get("logo_image"):
            try:
                img = Image.open(self.cleaned_data.get("logo_image"))
                width, height = img.size
                print('ololoolol', width, height)
                # Проверяем размер изображения в пикселях
                if width >= 1500 or height >= 900:
                    raise ValidationError(
                        f"Размер изображения слишком большой! Максимальный размер: 1500x900 пикселей. "
                        f"Загруженное изображение имеет размер: {width}x{height} пикселей."
                    )
            except Exception as e:
                raise ValidationError(f"Ошибка обработки изображения: {e}")


class LogoImageAdmin(admin.ModelAdmin):
    list_display = ["logo_image_preview"]
    form = ImageForm

    def logo_image_preview(self, obj):
        # Проверка, если поле obj.logo_image действительно существует
        if obj.logo_image:
            return format_html(
                '<img src="{}" style="max-height: 100px;" />', obj.logo_image.url
            )
        return "Нет изображения"

    logo_image_preview.short_description = "previews"


# Регистрация моделей
admin.site.register(models.Courses)
admin.site.register(models.ITCourses)
admin.site.register(models.LogoImage, LogoImageAdmin)
admin.site.register(models.Advanced)
admin.site.register(models.Welcome)
admin.site.register(models.Contact)
admin.site.register(models.News)
admin.site.register(models.Mission)
admin.site.register(models.OpenDoor)
