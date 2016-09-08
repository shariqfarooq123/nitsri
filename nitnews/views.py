from django.http import HttpResponse
from . import scrape

# Create your views here.
def get_news(response):
    return HttpResponse(scrape.get_news_json(),content_type='application/json')