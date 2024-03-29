from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('market.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()                                                             # only for development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)                         # only for development
