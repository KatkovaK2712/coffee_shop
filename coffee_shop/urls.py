from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cafe.urls')),
]

# Медиа-файлы (картинки из админки) отдаются только в режиме разработки.
# На продакшене (Fly.io) картинки лучше хранить во внешнем сервисе,
# либо использовать отдельное решение (Whitenoise умеет отдавать STATIC, но не MEDIA).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)