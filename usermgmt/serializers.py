from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUser


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    user_type = serializers.ChoiceField(
        CustomUser.SPECIAL_USER_CHOICES,
        source="customuser.user_type")
    password = serializers.CharField(
        max_length=128, write_only=True,
        style={'input_type': 'password'})
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        customuser = validated_data.pop("customuser")
        user = User.objects.create_user(**validated_data)
        user_type = customuser["user_type"]
        CustomUser.objects.create(user=user, user_type=user_type)
        return user

    class Meta:
        model = User