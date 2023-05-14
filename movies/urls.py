from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "Movie Api",
        default_version="v1",
        description="Api Django",
        terms_of_service="https://policies.google.com/terms",
        contact=openapi.Contact(email="angelo_stk06@hotmail.com"),
        license=openapi.License(name="MIT")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie', include("movie.urls")),
    path('user', include("user.urls")),
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name="swagger-docs")
]
