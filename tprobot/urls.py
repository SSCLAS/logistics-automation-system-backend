from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tprobot import views

router = DefaultRouter()
router.register(r'Robot', views.RobotViewSet)
router.register(r'Product', views.ProductViewSet)
router.register(r'Ware_house', views.Ware_houseViewSet)
router.register(r'Deliver_order', views.Deliver_orderViewSet)
router.register(r'Stock_order', views.Stock_orderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('Ware_house/<int:pk>/deliver', views.DeliverCreateView.as_view()),
]
