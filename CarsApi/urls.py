from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('CarsApi', views.PriceView)
urlpatterns = [
    path('', views.price_contact, name='price_contact'),
    path('api/', include(router.urls)),
    path('status/', views.price_reject),
]