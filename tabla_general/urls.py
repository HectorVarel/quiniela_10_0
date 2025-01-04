from django.urls import path
from tabla_general.views import tabla_general
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',  tabla_general, name='tabla_general'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)