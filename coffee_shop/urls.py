from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.http import JsonResponse
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cafe.urls')),
]

# Медиа-файлы отдаём через Django даже при DEBUG=False.
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]


# Временный маршрут для диагностики — покажет, что видит Django на сервере.
def debug_media(request):
    root = str(settings.MEDIA_ROOT)
    exists = os.path.exists(root)
    contents = []
    if exists:
        try:
            contents = sorted(os.listdir(root))
        except Exception as e:
            contents = [f'ERROR: {e}']

    # Проверим, есть ли конкретные файлы
    test_files = [
        'homepage/33c01df2e3aeb4d5cc96a008942a66ff.gif',
        'homepage/fd30846b19ff684f079d23b217a481e8.gif',
        'menu_items/811fdb30fbf89c2188e2994249a35c7e.jpg',
        'menu_items/2025-11-26_21-38-20_CCkjdkL.png',
    ]
    checks = {}
    for f in test_files:
        full = os.path.join(root, f)
        checks[f] = {
            'exists': os.path.exists(full),
            'is_file': os.path.isfile(full),
        }

    return JsonResponse({
        'BASE_DIR': str(settings.BASE_DIR),
        'MEDIA_ROOT': root,
        'exists': exists,
        'contents': contents,
        'test_files': checks,
    }, json_dumps_params={'indent': 2, 'ensure_ascii': False})

urlpatterns += [path('debug-media/', debug_media)]