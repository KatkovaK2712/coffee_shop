from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cafe.urls')),
]

# Медиа-файлы отдаём через Django даже при DEBUG=False.
# Для курсового проекта это ок. В реальном продакшене используют nginx/S3.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]