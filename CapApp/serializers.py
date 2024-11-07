# CapApp/serializers.py
from rest_framework import serializers
from .models import Vocabulary, User, Example
from django.contrib.auth.hashers import make_password

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['sentence']

class VocabularySerializer(serializers.ModelSerializer):
    examples = ExampleSerializer(many=True, read_only=True)

    class Meta:
        model = Vocabulary
        fields = ['_id', 'word', 'vietnamese', 'definition', 'category', 'examples']
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'username', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Mã hóa mật khẩu trước khi lưu
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)