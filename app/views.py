from django.shortcuts import render

# Create your views here.

def basic_calculator(request):
    return render(request, 'basic.html')

def scientific_calculator(request):
    return render(request, 'scientific.html')

def speed_calculator(request):
    return render(request, 'speed.html')

def height_calculator(request):
    return render(request, 'height.html')

def weight_calculator(request):
    return render(request, 'weight.html')

def distance_calculator(request):
    return render(request, 'distance.html')

def bmi_calculator(request):
    return render(request, 'bmi.html')

def temperature_converter(request):
    return render(request, 'temperature.html')

def area_calculator(request):
    return render(request, 'area.html')
