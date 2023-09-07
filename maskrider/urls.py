from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("todos/", include("todos.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
