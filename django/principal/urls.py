from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from api.views import CalendariosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('calendarios',CalendariosViewSet, basename='Calendarios')

urlpatterns = [
    path('', include('app.urls')),
    path('api/', include(router.urls) ),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )