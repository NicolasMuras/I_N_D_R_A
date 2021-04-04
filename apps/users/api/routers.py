from rest_framework.routers import DefaultRouter
from apps.users.api.views.views_user import UserViewSet


router = DefaultRouter()
router.register(r'Users', UserViewSet, basename = "Users")


urlpatterns = router.urls
