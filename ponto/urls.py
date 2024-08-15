from rest_framework.routers import DefaultRouter
from ponto.views import ImersionistaViewSet, PresencaViewSet

router = DefaultRouter()

router.register("imersionistas", ImersionistaViewSet, basename="imersionistas")

router.register("presencas", PresencaViewSet, basename="presencas")

urlpatterns = router.urls
