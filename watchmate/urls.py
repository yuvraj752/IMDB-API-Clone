from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('api/watch/', include('watchlist_app.api.urls')),
    path('api/account/', include('user_app.api.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # path('api-auth/', include('rest_framework.urls')),
]