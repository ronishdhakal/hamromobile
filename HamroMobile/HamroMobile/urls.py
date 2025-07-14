from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('api/brand/', include('brand.urls')),
    path('api/category/', include('category.urls')),
    path('api/segment/', include('segment.urls')),
    path('api/type/', include('type.urls')),
    path('api/phone/', include('phone.urls')),
    path('api/review/', include('review.urls')),
    path('api/news/', include('news.urls')),
    path('api/core/', include('core.urls')),
]

# ✅ ALWAYS serve static and media inside docker container
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
