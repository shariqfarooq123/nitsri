from django.http import JsonResponse
from . import scrape

# Create your views here.
def get_news(response):
    return JsonResponse(scrape.get_news_json(),content_type='application/json')