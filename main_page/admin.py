from django.utils.html import format_html
from django.contrib import admin
from . import models



#Чтобы было в админ панели видно фото
class LogoImageAdmin(admin.ModelAdmin):
    list_display = ['logo_image_preview']

    def logo_image_preview(self, obj):
        if obj.logo_image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.logo_image.url)
        return "Нет изображения"
    logo_image_preview.short_description = 'previews'


admin.site.register(models.Courses)
admin.site.register(models.ITCourses)
admin.site.register(models.LogoImage, LogoImageAdmin)
admin.site.register(models.Advanced)
admin.site.register(models.Welcome)
admin.site.register(models.Contact)
admin.site.register(models.News)
admin.site.register(models.Mission)
