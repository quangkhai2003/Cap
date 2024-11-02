from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Vocabulary
from .serializers import VocabularySerializer




@api_view(['GET'])
def VocabularyApi(request):
    vocabularies = Vocabulary.objects.all()
    serializer = VocabularySerializer(vocabularies, many=True)
    return Response(serializer.data)

    # elif request.method == 'POST':
    #     vocabulary_data = JSONParser().parse(request)
    #     vocabulary_serializer = VocabularySerializer(data=vocabulary_data)
    #     if vocabulary_serializer.is_valid():
    #         vocabulary_serializer.save()
    #         return JsonResponse("Added Successfully", safe=False)
    #     return JsonResponse("Failed to Add", safe=False)
    
    # elif request.method == 'PUT':
    #     vocabulary_data = JSONParser().parse(request)
    #     try:
    #         vocabulary = Vocabulary.objects.get(id=vocabulary_data['id'])
    #     except Vocabulary.DoesNotExist:
    #         return JsonResponse("Vocabulary not found", safe=False)
        
    #     vocabulary_serializer = VocabularySerializer(vocabulary, data=vocabulary_data)
    #     if vocabulary_serializer.is_valid():
    #         vocabulary_serializer.save()
    #         return JsonResponse("Updated Successfully", safe=False)
    #     return JsonResponse("Failed to Update", safe=False)
    
    # elif request.method == 'DELETE':
    #     try:
    #         vocabulary = Vocabulary.objects.get(id=id)
    #         vocabulary.delete()
    #         return JsonResponse("Deleted Successfully", safe=False)
    #     except Vocabulary.DoesNotExist:
    #         return JsonResponse("Vocabulary not found", safe=False)