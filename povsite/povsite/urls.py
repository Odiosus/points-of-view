from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gallery.urls'))
]


admin.site.site_header = 'Арт-лаборатория "Точки Зрения", открывающая искусство по-новому'
admin.site.site_title = 'Лаборатория "Точки Зрения"'
