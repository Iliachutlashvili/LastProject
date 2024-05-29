from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', core_views.index, name='books'),
    path('register/', core_views.register, name='register'),
    path('login/', core_views.custom_login, name='login'),
    path('profile/', core_views.profile, name='profile'),
    path('logout/', core_views.custom_logout, name='logout'),
    path('', core_views.index, name='index'),
]
