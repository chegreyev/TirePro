from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('producers', viewset=ProducerViewSet, basename='Изготовитель')
router.register('tires', viewset=TireViewSet, basename='Шины')


urlpatterns = router.urls