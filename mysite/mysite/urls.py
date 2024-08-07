from django.contrib import admin
from django.urls import (include, path)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("reactpy/", include("reactpy_django.http.urls")),
    path('', include('reactpy_drf.urls')),
]
