from rest_framework import serializers

from .models import ContactUs


class ContactUserializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

    def create(self, validated_data):
        return ContactUs.objects.create(**validated_data)