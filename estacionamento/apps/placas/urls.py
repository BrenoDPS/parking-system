from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlacaDetectadaViewSet, PlacaDetectadaCreateView

router = DefaultRouter()
router.register(r'placas', PlacaDetectadaViewSet, basename='placa')

urlpatterns = [
    path('registrar_placa/', PlacaDetectadaCreateView.as_view(), name='registrar_placa'),
    path('', include(router.urls)),
]