from rest_framework import routers, serializers, viewsets
from Stock.viewsets import CategoriaViewSet

router = routers.DefaultRouter()

router.register(r´categoria´, CategoriaViewSet)