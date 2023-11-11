from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls), path("bot/", include("bot.urls")),
    path('sentry-debug/', trigger_error),
]

if settings.DEBUG:
    urlpatterns += [
        *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]
