from django.urls import path
from web.views import index, about, welcome, contact

urlpatterns = [
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenido/', welcome, name='welcome'),
    path('contacto/', contact, name='contact'),
]