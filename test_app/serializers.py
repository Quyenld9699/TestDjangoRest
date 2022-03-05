from rest_framework import serializers
from .models import TestModel

class SimpleviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    phone = serializers.IntegerField()
    is_live = serializers.BooleanField()
    amount = serializers.FloatField()
    extra_name = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return TestModel.objects.create(**validated_data)
    def update(self, instance, validated_data):
        TestModel.objects.filter(id=instance.id).update(**validated_data)
        return TestModel.objects.get(id=instance.id)


class SimpleModalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        # fields = ("name", "description")
        fields = "__all__"