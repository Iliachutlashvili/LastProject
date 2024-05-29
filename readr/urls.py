from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('book.urls')),
    path('authors/', include('author.urls')),
    path('register/', core_views.register, name='register'),
    path('login/', core_views.custom_login, name='login'),
    path('profile/', core_views.profile, name='profile'),
    path('logout/', core_views.custom_logout, name='logout'),
    path('', core_views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)