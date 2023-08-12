from rest_framework.viewsets import ReadOnlyModelViewSet

from api.v1.nec.serializers import SubjectSerializer
from nec.models import NECSubject, ModelSet, Question


class NECSubjectViewset(ReadOnlyModelViewSet):
    queryset = NECSubject.objects.all()
    serializer_class = SubjectSerializer
