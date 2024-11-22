from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework import status

from .models import Vocabulary, User, Example, Topic
from .serializers import VocabularySerializer, ExampleSerializer
from .serializers import RegisterSerializer, LoginSerializer


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

@api_view(['GET'])
def get_vocabulary_by_topic(request, topic):
    try:
        # Lấy tất cả các từ vựng
        all_vocabularies = Vocabulary.objects.all()
        
        # Lọc các từ vựng theo topic
        filtered_vocabularies = [vocab for vocab in all_vocabularies if vocab.topic == topic]
        
        # Nếu không có từ vựng thuộc topic
        if not filtered_vocabularies:
            return Response({'error': f'No vocabulary found for topic "{topic}"'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize dữ liệu
        serializer = VocabularySerializer(filtered_vocabularies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def add_multiple_vocabularies(request):
    if request.method == 'POST':
        data = request.data  # Lấy dữ liệu JSON
        if isinstance(data, list):
            created_vocabularies = []
            for vocab_data in data:
                serializer = VocabularySerializer(data=vocab_data)
                if serializer.is_valid():
                    serializer.save()
                    created_vocabularies.append(serializer.data)
                else:
                    # Log lỗi nếu validation không thành công
                    print("Validation Errors:", serializer.errors)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(created_vocabularies, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Expected a list of vocabularies'}, status=status.HTTP_400_BAD_REQUEST)

    
# @api_view(['POST'])
# def add_vocabulary_to_topic(request, topic_name):
#     try:
#         # Tìm kiếm Topic dựa trên tên
#         topic = Topic.objects.get(name=topic_name)
#     except Topic.DoesNotExist:
#         # Trả về thông báo nếu không tìm thấy Topic
#         return Response({'error': f'Topic with name "{topic_name}" not found'}, status=status.HTTP_404_NOT_FOUND)

#     # Sao chép dữ liệu và thêm category_id
#     data = request.data.copy()
#     data['category'] = topic.id  # Gán id của topic vào trường category của Vocabulary

#     # Khởi tạo serializer với dữ liệu đã chỉnh sửa
#     serializer = VocabularySerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully", "pin": serializer.data.get("pin")},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

