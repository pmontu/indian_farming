from rest_framework import viewsets
from rest_framework import mixins

from .serializers import AccountSerializer
from .models import Account
from .permissions import AllowSpecialUsersToCreateOnlyAdminUsersToList


class AccountViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin, 
                     viewsets.GenericViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = (AllowSpecialUsersToCreateOnlyAdminUsersToList, )