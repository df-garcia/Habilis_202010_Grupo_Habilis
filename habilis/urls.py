from django.contrib import admin
from django.urls import path, include
from . import views,auth0backend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('medicamentos/', include('medicamentos.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('eps/', include('eps.urls')),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
    path('autenticado/', views.measurement_list)
]
