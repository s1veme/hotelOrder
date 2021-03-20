from rest_framework import serializers

from ..models import Review


class ReviewSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
