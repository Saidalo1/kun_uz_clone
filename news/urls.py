from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from news.views.blog import BlogDocumentViewSet
from news.views.blog_handbook import CategoryViewSet, RegionViewSet
from root import settings

router = DefaultRouter()
# router.register('blog', BlogModelViewSet, 'blog')
router.register('blog', BlogDocumentViewSet, 'blog-2')
router.register('category', CategoryViewSet, 'category')
router.register('region', RegionViewSet, 'region')

urlpatterns = [
                  path('', include(router.urls))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
