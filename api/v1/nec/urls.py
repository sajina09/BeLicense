from rest_framework.routers import DefaultRouter
from api.v1.nec.viewsets import NECSubjectViewset
from django.urls import path, include


router = DefaultRouter()
router.register(r"subjects", NECSubjectViewset)


urlpatterns = [
    path('', include(router.urls))
]
