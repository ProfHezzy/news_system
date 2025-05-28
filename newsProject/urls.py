<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newsApp.urls'))
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
=======
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newsApp.urls'))
] + static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
>>>>>>> 784256ef5fbcc3d56a7a2831162e02964209c51b
