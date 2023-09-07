from rest_framework.viewsets import ModelViewSet

from api.v1.nec.serializers import SubjectSerializer, ModelSetSerializer
from nec.models import NECSubject, ModelSet


class NECSubjectViewset(ModelViewSet):
    queryset = NECSubject.objects.all()
    serializer_class = SubjectSerializer

class ModelSetViewset(ModelViewSet):
    queryset = ModelSet.objects.all()
    serializer_class = ModelSetSerializer
   

