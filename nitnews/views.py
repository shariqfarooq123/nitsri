from django.http import HttpResponse
import json 
from . import scrape

# Create your views here.
def get_news(response):
    return HttpResponse("<h1>Hello world</h1>")
    #return JsonResponse(scrape.get_news_json(),content_type='application/json')