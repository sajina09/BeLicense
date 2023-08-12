from django.urls import path, include
from api.v1.nec.urls import urlpatterns as nec_urlpatterns

urlpatterns = [
    path("nec/", include(nec_urlpatterns))
]