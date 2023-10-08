from rest_framework import serializers
from nec.models import NECSubject, Question, ModelSet, Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["topic_name"]


class SubjectSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True, source='topic')

    class Meta:
        model = NECSubject
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    syllabus = serializers.SerializerMethodField()

    class Meta:
        model = NECSubject
        fields = "__all__"

    def get_syllabus(self, obj):
        syllabus_dict = {}
        for chapter in obj.syllabus.filter(parent_chapter__isnull=True):
            chapter_name = chapter.chapter_name
            subchapters = {}
            for subchapter in obj.syllabus.filter(parent_chapter=chapter):
                subchapter_name = subchapter.chapter_name
                topics = [
                    topic.topic_name for topic in subchapter.topic_set.all()]
                subchapters[subchapter_name] = topics
            syllabus_dict[chapter_name] = subchapters
        return syllabus_dict


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ModelSetListSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(
        source="subject.subject_name", read_only=True)

    class Meta:
        model = ModelSet
        fields = ["id", "set_name", "subject_name", "model_set_link"]


class ModelSetSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = ModelSet
        fields = ["set_name", "questions"]
