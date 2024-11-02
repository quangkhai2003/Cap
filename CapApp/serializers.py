# CapApp/serializers.py
from rest_framework import serializers
from .models import Vocabulary

class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ['_id', 'word', 'vietnamese', 'definition', 'examples', 'category']
