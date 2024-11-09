from django.utils.html import format_html
from django.contrib import admin
from . import models



class LogoImageAdmin(admin.ModelAdmin):
    list_display = ['logo_image_preview']

    def logo_image_preview(self, obj):
        # Проверка, если поле obj.logo_image действительно существует
        if obj.logo_image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.logo_image.url)
        return "Нет изображения"

    logo_image_preview.short_description = 'previews'

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
