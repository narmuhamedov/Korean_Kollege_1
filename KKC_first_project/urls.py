from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("stalker/", admin.site.urls),
    path("", include("main_page.urls")),
    path("", include("documents.urls")),
    path("", include("about_us.urls")),
    path("", include("international_department.urls")),
    path("", include("abiturients.urls")),
    path("", include("stud_live.urls")),
    path("", include("blog.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
