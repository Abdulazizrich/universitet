from django.contrib import admin
from django.urls import path
from tatu.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fan/',fans),
    path('ustoz/',teacher),
    path('kurs/', kurs),
    path('edit/<int:id>/tahrirlash/', fan_tahrirlash),
    path('edit1/<int:id>/tahrirlash/', ustoz_tahrirlash),
    path('edit2/<int:id>/tahrirlash/', kurs_tahrirlash),
]
