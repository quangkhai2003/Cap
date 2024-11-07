from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework import status

from .models import Vocabulary, User, Example
from .serializers import VocabularySerializer, ExampleSerializer
from .serializers import RegisterSerializer, LoginSerializer



# View cho Vocabulary
@api_view(['GET', 'POST'])
def VocabularyApi(request):
    if request.method == 'GET':
        vocabularies = Vocabulary.objects.all()
        serializer = VocabularySerializer(vocabularies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VocabularySerializer(data=request.data)
        if serializer.is_valid():
            vocabulary = serializer.save()
            return Response(VocabularySerializer(vocabulary).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def ExamplesByWordApi(request, word):
    try:
        vocabulary = Vocabulary.objects.get(word=word)
    except Vocabulary.DoesNotExist:
        return Response({"error": "Vocabulary not found"}, status=status.HTTP_404_NOT_FOUND)

    examples = Example.objects.filter(vocabulary=vocabulary)
    serializer = ExampleSerializer(examples, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def AddExampleByWordApi(request, word):
    try:
        vocabulary = Vocabulary.objects.get(word=word)
    except Vocabulary.DoesNotExist:
        return Response({"error": "Vocabulary not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ExampleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(vocabulary=vocabulary)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def VocabularyByWordApi(request, word):
    try:
        vocabulary = Vocabulary.objects.get(word=word)
        serializer = VocabularySerializer(vocabulary)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Vocabulary.DoesNotExist:
        return Response({"error": "Vocabulary not found"}, status=status.HTTP_404_NOT_FOUND)
    
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# views.py
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            try:
                user = User.objects.get(username=username)
                # Kiểm tra mật khẩu
                if check_password(password, user.password):
                    return Response({"message": "Login successful", "user_id": user._id}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Invalid password"}, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

