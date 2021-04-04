from rest_framework.routers import DefaultRouter
from apps.Tags.api.views.views_tags import TagViewSet


router = DefaultRouter()
router.register(r'Tags', TagViewSet, basename = "Tags")


urlpatterns = router.urls
