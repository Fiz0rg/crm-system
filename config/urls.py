from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="CRM API",
      default_version='v1',
      description="API for crm system open source project",
      contact=openapi.Contact(email="so.gorich@inbox.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/v1/', include('crm.urls')),
    path('api-auth/', include('rest_framework.urls')),
]


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    urlpatterns.extend(
        (
            path('admin/', admin.site.urls),
            path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        )
    )
