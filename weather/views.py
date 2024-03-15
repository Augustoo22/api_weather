from datetime import datetime
from random import randrange
from django.shortcuts import render
from django.views import View
from weather.models import WeatherEntity

class WeatherView(View):
    def get(self, request):
        weathers = []
        for i in range(10):
            weathers.append(
                WeatherEntity(
                    temperature=randrange(start=17, stop=40),
                    date=datetime.now()
                )
            )
        
        # Renderiza o template 'clima.html' localizado na pasta 'templates' da aplicação 'climaApp'
        return render(request, 'clima.html', {'weathers': weathers})
