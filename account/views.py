from rest_framework import viewsets
from rest_framework import mixins

from .serializers import AccountSerializer


class AccountViewSet(mixins.CreateModelMixin, 
				   viewsets.GenericViewSet):
	serializer_class = AccountSerializer