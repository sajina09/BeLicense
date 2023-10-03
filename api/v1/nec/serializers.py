from rest_framework import serializers
from nec.models import NECSubject, Question, ModelSet


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NECSubject
        fields = "__all__"
        # fields = ['subject_name']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ModelSetListSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source="subject.subject_name", read_only=True)
    class Meta:
        model = ModelSet
        fields = ["id", "set_name", "subject_name"]


class ModelSetSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = ModelSet
        fields = ["set_name", "questions"]
