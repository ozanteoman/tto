from rest_framework import serializers
from ..models import Posts

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields=["id","title","user","content","created_date"]

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields=["user","title","content"]
        read_only_fields=["user"]