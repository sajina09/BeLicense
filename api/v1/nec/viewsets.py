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
        # try:
        # num_group_a = int(request.query_params.get('num_group_a', 5))
        # num_group_b = int(request.query_params.get('num_group_b', 5))
        if a_count := request.query_params.get("a_count") or None:
            a_count = int(a_count)
        if b_count := request.query_params.get("b_count") or None:
            b_count = int(a_count)
        # shuffle_questions = request.query_params.get(
        #     'shuffle_questions', 'false').lower() == 'true'

        model_set = self.get_object()

        q = model_set.questions.none()
        for grp, count in (("a", a_count), ("b", b_count)):
            q |= model_set.questions.filter(group=grp).order_by("?")[:count]

        return Response({"questions": QuestionSerializer(q, many=True).data})

            # Get questions for Group A
        #     group_a_questions = model_set.questions.filter(group='a')[
        #         :num_group_a]
        #
        #     # Get questions for Group B
        #     group_b_questions = model_set.questions.filter(group='b')[
        #         :num_group_b]
        #     print("----group_b_questions", group_b_questions)
        #     if shuffle_questions:
        #         # Shuffle the questions if shuffle_questions is True
        #         group_a_questions = list(group_a_questions)
        #         group_b_questions = list(group_b_questions)
        #         random.shuffle(group_a_questions)
        #         random.shuffle(group_b_questions)
        #
        #     # Serialize questions and data
        #     serialized_group_a = QuestionSerializer(
        #         group_a_questions, many=True)
        #     serialized_group_b = QuestionSerializer(
        #         group_b_questions, many=True)
        #
        #     # Construct the response dictionary
        #     response_data = {
        #         'data': {
        #             'group_a_questions': serialized_group_a.data,
        #             'group_b_questions': serialized_group_b.data,
        #             'shuffle_questions': shuffle_questions,
        #         },
        #         'message': 'Customized questions fetched successfully',
        #         'success': True,
        #     }
        #
        #     return JsonResponse(response_data)
        #
        # except ModelSet.DoesNotExist:
        #     response_data = {
        #         'data': {},
        #         'message': 'ModelSet not found',
        #         'success': False,
        #     }
        #     return JsonResponse(response_data, status=404)
        # except Exception as e:
        #     response_data = {
        #         'data': {},
        #         'message': str(e),  # You can customize the error message here
        #         'success': False,
        #     }
        #     return JsonResponse(response_data, status=500)

    # # def get_single_modelset(self, request, pk=None):
    #     try:
    #         # Get the query parameter 'subject_filter'
    #         subject_filter = request.query_params.get('subject_filter', '')

    #         # Retrieve the ModelSet object
    #         model_set = self.get_object()

    #         # Filter subjects based on the 'subject_filter' parameter
    #         filtered_subjects = NECSubject.objects.filter(
    #             Q(name__icontains=subject_filter)
    #         )

    #         # Now you can use 'filtered_subjects' in your response or processing logic
    #         # ...

    #         # Your response data here
    #         response_data = {
    #             'data': {
    #                 # Include filtered_subjects data in the response as needed
    #             },
    #             'message': 'ModelSet data fetched successfully',
    #             'success': True,
    #         }

    #         return JsonResponse(response_data)

    #     except ModelSet.DoesNotExist:
    #         response_data = {
    #             'data': {},
    #             'message': 'ModelSet not found',
    #             'success': False,
    #         }
    #         return JsonResponse(response_data, status=404)
    #     except Exception as e:
    #         response_data = {
    #             'data': {},
    #             'message': str(e),
    #             'success': False,
    #         }
    #         return JsonResponse(response_data, status=500)
