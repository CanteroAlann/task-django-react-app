from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("task.urls", namespace="task")),
    path('api-auth/', include('rest_framework.urls')),
]
