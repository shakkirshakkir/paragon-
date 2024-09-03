from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class ChatSerializer(serializers.Serializer):
    participants = models.ManyToManyField(User, related_name='chats')
    created_at = models.DateTimeField(auto_now_add=True)
  

    
class ChatModelSer(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields="__all__"

   

class UserModelSer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


