# CapApp/serializers.py
from rest_framework import serializers
from .models import Vocabulary, User, Example, Topic
from django.contrib.auth.hashers import make_password

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['name', 'vietnamese']
        
class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['sentence']

class VocabularySerializer(serializers.ModelSerializer):
    examples = ExampleSerializer(many=True, read_only=True)
    
    class Meta:
        model = Vocabulary
        fields = ['_id', 'word', 'vietnamese', 'definition', 'examples', 'topic']
    
    def create(self, validated_data):
        # Xử lý dữ liệu examples
        examples_data = validated_data.pop('examples', [])
        vocabulary = Vocabulary.objects.create(**validated_data)  # Tạo vocabulary
        
        # Tạo từng câu ví dụ
        for example_data in examples_data:
            Example.objects.create(vocabulary=vocabulary, **example_data)
        
        return vocabulary
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'phone', 'password', 'pin']
        extra_kwargs = {'password': {'write_only': True}, 'pin': {'required': False}}

    def create(self, validated_data):
        # Nếu không có mã PIN được gửi, sử dụng giá trị mặc định
        pin = validated_data.get('pin', '123456')
        validated_data['pin'] = pin
        return User.objects.create(**validated_data)
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)