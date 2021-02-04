from django.shortcuts import render
from django.http import HttpResponse
from books.models import Cities

def home_page(request):
    city = Cities.objects.last()
    context = {"city": city}
    return render(request, template_name = 'home.html', context = context)
    #return HttpResponse(f"The first city is {city.name} with pk = {city.pk}")