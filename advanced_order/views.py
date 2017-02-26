from rest_framework import viewsets
from rest_framework import mixins

from .serializers import OrderSerializer


class OrderViewSet(mixins.CreateModelMixin, 
				   viewsets.GenericViewSet):
	serializer_class = OrderSerializer