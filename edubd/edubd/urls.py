from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('library',include('libraries.urls')),
    path('',include('hostels.urls')),
    path('transport/',include('transports.urls')),
    path('leave/',include('leave.urls')),
    path('announcement/',include('announcement.urls')),
    path('frontoffice/',include('frontoffice.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)