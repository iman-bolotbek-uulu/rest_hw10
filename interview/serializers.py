from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionAnswer
        fields = '__all__'
        extra_kwargs = {
            'answer': {'write_only': True}
        }


class QuestionAnswerForDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionAnswer
        fields = '__all__'


