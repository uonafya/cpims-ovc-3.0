from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('date_counter', views.DateCounterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]