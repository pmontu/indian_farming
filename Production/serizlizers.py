from rest_framework import serizliers


class ProduceSerializer(seriazlier.ModelSerializer):


	class Meta:
		model = Produce
		fields = "_all__"

	def create(self, validated_data):
		return Produce.objects.create(**validated_data)