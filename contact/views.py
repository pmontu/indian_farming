from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import permissions

from .serializers import ContactUserializer
from .models import ContactUs
from .permissions import OnlyAllowAnyOneToSubmit


class ContactUsViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    serializer_class = ContactUserializer
    queryset = ContactUs.objects.all()
    permission_classes = (OnlyAllowAnyOneToSubmit, )