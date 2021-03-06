from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('producers', viewset=ProducerViewSet, basename='Изготовитель')
router.register('tires', viewset=TireViewSet, basename='Шины')
router.register('cars', viewset=CarViewSet, basename='Машины')
router.register('discs', viewset=DiscViewSet, basename='Диски')

urlpatterns = router.urls