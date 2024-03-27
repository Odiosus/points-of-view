from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import GalleryList, GalleryViewSet, GalleryDetail
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'gallery', GalleryViewSet)



urlpatterns = [
    path('', GalleryList.as_view(), name='main'),
    path('projects/<int:pk>', GalleryDetail.as_view(), name='detail'),
    path('api/', include(router.urls), name='api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
