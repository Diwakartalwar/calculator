from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.basic_calculator, name='home'),
    path('basic/', views.basic_calculator, name='basic'),
    path('scientific/', views.scientific_calculator, name='scientific'),
    path('speed/', views.speed_calculator, name='speed'),
    path('height/', views.height_calculator, name='height'),
    path('weight/', views.weight_calculator, name='weight'),
    path('distance/', views.distance_calculator, name='distance'),
    path('bmi/', views.bmi_calculator, name='bmi'),
    path('temperature/', views.temperature_converter, name='temperature'),
    path('area/', views.area_calculator, name='area'),
] 