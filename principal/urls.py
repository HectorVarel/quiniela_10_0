from django.urls import path
from principal.views import principal
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('',  principal, name='principal'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)