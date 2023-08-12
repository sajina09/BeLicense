from rest_framework.viewsets import ModelViewSet

from api.v1.nec.serializers import SubjectSerializer
from nec.models import NECSubject, ModelSet, Question


class NECSubjectViewset(ModelViewSet):
    queryset = NECSubject.objects.all()
    serializer_class = SubjectSerializer
