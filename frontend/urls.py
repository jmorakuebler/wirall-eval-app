from django.urls import path

from . import views


app_name = "frontend"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('persons/', views.PersonView.as_view(), name="persons"),
]
