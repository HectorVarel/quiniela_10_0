from django.urls import path
from jornadas.views import jornadas
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',  jornadas, name='jornadas'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)