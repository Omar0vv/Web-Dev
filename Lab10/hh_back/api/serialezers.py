from rest_framework import serializers
from .models import Company, Vacancy


class CompanySerializerS(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()


class VacancySerializerS(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    salary = serializers.IntegerField()


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description')

    def create(self, validated_data):
        print(validated_data)
        return 1

    def update(self, instance, validated_data):
        pass


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'salary', 'company')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass