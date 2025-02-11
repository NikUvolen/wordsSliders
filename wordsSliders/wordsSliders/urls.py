from django.contrib import admin
from django.urls import path, include

from debug_toolbar.toolbar import debug_toolbar_urls

from .settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('a_sliders.urls'))
]

if DEBUG:
    urlpatterns += debug_toolbar_urls()
