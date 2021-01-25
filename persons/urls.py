from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


app_name = "persons"

router = DefaultRouter()
router.register('persons', views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
