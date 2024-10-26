from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# apps
from apps.notification.views import notifications_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("apps.base.urls")),
    path("api/v1/users/", include("apps.users.urls")),
    path("api/v1/notification/", include("apps.notification.urls")),
    path('notifications/', notifications_page, name='notifications_page'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)