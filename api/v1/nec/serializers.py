from rest_framework import serializers
from nec.models import NECSubject, Question, ModelSet


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NECSubject
        fields = "__all__"


# class ModelSetSerializer(serializers):
#     pass