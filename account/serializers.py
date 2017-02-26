from rest_framework import serializers

from usermgmt.models import CustomUser
from .models import Account

class AccountSerializer(serializers.ModelSerializer):


	class Meta:
		model = Account
		fields = "__all__"
		read_only_fields = ('entry_by', 'entry',)

	def create(self, validated_data):
		entry_by = self.context["request"].user
		entry = None
		if entry_by.customuser.user_type == CustomUser.CUSTOMER:
			entry = CustomUser.CUSTOMER
		elif entry_by.customuser.user_type == CustomUser.FARMER:
			entry = CustomUser.FARMER
		validated_data["entry_by"] = entry_by
		validated_data["entry"] = entry
		return Account.objects.create(**validated_data)