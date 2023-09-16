from rest_framework.routers import DefaultRouter
from api.v1.nec.viewsets import NECSubjectViewset, ModelSetViewset
from django.urls import path, include

router = DefaultRouter()
router.register(r"subjects", NECSubjectViewset)
router.register(r'modelsets', ModelSetViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('modelsets/<int:pk>/',
         ModelSetViewset.as_view({'get': 'get_single_modelset'}), name='modelset-detail'),
    path('modelsets/<int:pk>/get_customized_questions/', ModelSetViewset.as_view(
        {'get': 'get_customized_questions'}), name='modelset-custom-questions'),
]
