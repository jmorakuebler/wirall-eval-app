from django.urls import path, include

from rest_framework.routers import DefaultRouter


from . import views


app_name = 'cards'

router = DefaultRouter()
router.register('cards', views.CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
