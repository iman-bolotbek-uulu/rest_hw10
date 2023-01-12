from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

from . import models
from . import serializers


class QuestionPagePagination(PageNumberPagination):
    page_size = 3


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class QuestionAnswerListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.QuestionAnswer.objects.all()
    serializer_class = serializers.QuestionAnswerSerializer
    pagination_class = QuestionPagePagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['question', 'category']
    ordering_fields = ['importance', ]

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        question = self.request.query_params.get('question')
        if question and category:
            queryset = queryset.filter(Q(question__icontains=question) & Q(category=category))
        return queryset


class QuestionAnswerForDetailViewSet(generics.RetrieveUpdateAPIView):
    queryset = models.QuestionAnswer.objects.all()
    serializer_class = serializers.QuestionAnswerForDetailSerializer

