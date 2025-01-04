from django.urls import path
from llenar_quiniela.views import ingresar_resultado
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',  ingresar_resultado, name='ingresar_resultado'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)