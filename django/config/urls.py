from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('apps.api.urls')),
    path('hotfix/', include('libs.hotfix.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    prefix_default_language=False,
)

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
