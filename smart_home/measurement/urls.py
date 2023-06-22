from django.urls import path

from .views import SensorCreateView, SensorUpdateView, MeasurementView

urlpatterns = [
    path("sensors/", SensorCreateView.as_view()),
    path("sensors/<pk>", SensorUpdateView.as_view()),
    path("measurements/", MeasurementView.as_view()),
]

