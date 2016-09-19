from django.conf.urls.defaults import url
from . import views

urlpatterns = [
    url(r'^$', views.get_news),
]
