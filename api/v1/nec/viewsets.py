from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework.response import Response
import random  # Import random module

from api.v1.nec.serializers import SubjectSerializer, ModelSetListSerializer, ModelSetSerializer, QuestionSerializer
from nec.models import NECSubject, ModelSet


class NECSubjectViewset(ModelViewSet):
    queryset = NECSubject.objects.all()
    serializer_class = SubjectSerializer


class ModelSetViewset(ModelViewSet):
    queryset = ModelSet.objects.all()
    serializer_class = ModelSetSerializer

    def get_queryset(self):
        q = self.queryset
        if subject_id := self.request.query_params.get("subject"):
            return q.filter(subject_id=subject_id)
        return q

    def get_serializer_class(self):
        if (self.get_view_name() or "").lower().endswith("list"):
            return ModelSetListSerializer
        else:
            return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        if a_count := request.query_params.get("a_count") or None:
            a_count = int(a_count)
        if b_count := request.query_params.get("b_count") or None:
            b_count = int(a_count)

        model_set = self.get_object()

        q = model_set.questions.none()
        for grp, count in (("a", a_count), ("b", b_count)):
            q |= model_set.questions.filter(group=grp).order_by("?")[:count]

        return Response({"questions": QuestionSerializer(q, many=True).data})
