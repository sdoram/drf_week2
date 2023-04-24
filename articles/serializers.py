from .models import Article
from rest_framework import serializers
# 시리얼라이저 임포트

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
