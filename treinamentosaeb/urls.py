from django.contrib import admin
from django.urls import path
from saeb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_cadastro, name='login'),
]
