from rest_framework import mixins, viewsets

from .serializers import ProduceSerializer


class ProduceViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
	serializer_class = ProduceSerializer