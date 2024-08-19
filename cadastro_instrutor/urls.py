from rest_framework.routers import DefaultRouter

from .views import CreateUsersViewSet

router = DefaultRouter()

router.register(r"", CreateUsersViewSet, basename="create_users")

urlpatterns = router.urls
