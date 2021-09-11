from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "Core"

urlpatterns = [
    path("", views.uploadFile, name = "uploadFile"),
    path('upload/', views.upload_files, name = "upload_files"),
    path('query/', views.query_files, name = "query_files"),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )

