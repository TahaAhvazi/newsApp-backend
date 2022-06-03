from ast import Try
import imp
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from article import serializers
from article.models import Article
from rest_framework import status
from article.serializers import ArticleSerializer

#Get a list of all articles 

class ArticleList(APIView):
    def get(self , request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles , many=True)
        return Response(serializer.data)

class ArticleDeatil(APIView):
    def get(self, request, pk):
            articles = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(articles)
            return Response(serializer.data)