import os
import requests
from django.shortcuts import render, redirect
from dotenv import load_dotenv
from django.contrib import messages

load_dotenv()

PAKISTAN_CITIES = [
    'Karachi', 'Lahore', 'Islamabad', 'Rawalpindi', 'Faisalabad', 
    'Multan', 'Peshawar', 'Quetta', 'Sialkot', 'Gujranwala',
    'Hyderabad', 'Abbottabad', 'Sargodha', 'Bahawalpur', 'Sukkur'
]

def index(request):
    context = {'cities': PAKISTAN_CITIES}
    
    if request.method == 'POST':
        city = request.POST.get('city', '')
        api_key = os.getenv('OPENWEATHER_API_KEY')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city},PK&appid={api_key}&units=metric'
        
        try:
            response = requests.get(url)
            weather_data = response.json()

            if response.status_code == 200:
                context.update({
                    'city': city,
                    'temperature': round(weather_data['main']['temp']),
                    'description': weather_data['weather'][0]['description'],
                    'icon': weather_data['weather'][0]['icon'],
                    'humidity': weather_data['main']['humidity'],
                    'wind_speed': weather_data['wind']['speed']
                })
            else:
                context['error'] = 'City not found'
        except Exception as e:
            context['error'] = str(e)
    
    return render(request, 'weather/index.html', context)

def city_weather(request, city):
    api_key = os.getenv('OPENWEATHER_API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        data = {
            'city': city,
            'temperature': round(weather_data['main']['temp']),
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }
    else:
        data = {'error': 'City not found'}
    return render(request, 'weather/index.html', data)

def search_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city', '')
        return redirect('city_weather', city=city)
    return redirect('index')
