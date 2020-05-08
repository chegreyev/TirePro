from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter
router.register('producers', ProducerViewSet, basename='Изготовитель')
router.register('tires', TireViewSet, basename='Шины')


urlpatterns = router.urls