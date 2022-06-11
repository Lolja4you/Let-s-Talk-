from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('article.urls')),
    path('', include('users.urls')),
    #path('', include('analytics.urls')),
    path('', include('ChatSystem.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
