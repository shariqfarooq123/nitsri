from django.http import JsonResponse
import json 
from . import scrape

# Create your views here.
def get_news(response):
    return JsonResponse(json.dumps('{"hey":"hello"}'),safe=False)
    #return JsonResponse(scrape.get_news_json(),content_type='application/json')