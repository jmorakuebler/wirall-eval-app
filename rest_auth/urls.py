from django.urls import path

from . import views


app_name = 'rest_auth'

urlpatterns = [
    path('drf-token/', views.CreateDRFTokenView.as_view(), name='drf-token'),
]
