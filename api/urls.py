from api.v1.urls import urlpatterns as v1_urls
from django.urls import path, include

urlpatterns = [
    path("v1/", include(v1_urls))
]