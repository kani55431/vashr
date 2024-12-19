from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("usersapp.urls")),
    path("punchingattendance/", include("attendance.urls")),
    path("employee/", include("employee.urls")),
    path("payroll/", include("audit.urls")),
    path("admin/", admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)