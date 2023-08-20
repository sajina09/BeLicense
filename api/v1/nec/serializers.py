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

class ModelSetSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = ModelSet
        fields = '__all__'
