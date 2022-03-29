from django.urls import path, re_path
from . import views


urlpatterns = [
    path("", views.inicio, name='inicio'),
    path("home", views.inicio, name='inicio'),
    re_path(r'^home/orderBy/(?P<order>(nombre|apellidos|fecha_nacio))$', views.home, name='home'),
    path('contacto/nuevo', views.contacto_nuevo, name='contacto_nuevo'),
    path('contacto/<int:pk>/edit', views.contacto_edicion, name='contacto_edicion'),
    path('contacto/<int:pk>/direccion', views.direccion_edicion, name='direccion_edicion'),
    path('contacto/<int:pk>/eliminar', views.contacto_eliminar, name='contacto_eliminar'),
    path('contacto/<int:pk>/telefono', views.telefonos_edicion, name='telefonos_edicion'),


]
