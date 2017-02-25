from django.contrib.auth.models import User
from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.Serializer):
	username = serializers.CharField()
	user_type = serializers.ChoiceField(
		CustomUser.SPECIAL_USER_CHOICES,
		source="customuser.user_type")

	class Meta:
		model = User