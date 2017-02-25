from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import mixins

from .serializers import UserSerializer

class UserViewSet(
		mixins.ListModelMixin,
		viewsets.GenericViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()