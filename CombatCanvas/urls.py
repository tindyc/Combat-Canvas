from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('projects/', include('projects.urls')),
    path('users/', include('users.urls')),
    path('contact', include('contact.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

