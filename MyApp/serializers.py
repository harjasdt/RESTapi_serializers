from rest_framework import serializers
from .models import UserProfile,Post

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields='__all__'


class PostSerializer(serializers.ModelSerializer):
    nested_author=UserProfileSerializer(many=True,read_only=True)
    class Meta:
        model=Post
        fields=['title','content','created_at','nested_author']