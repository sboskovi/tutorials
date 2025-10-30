from rest_framework import serializers

from base.models import ItemModel, Employee, Company, ITEM_TYPES


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.StringRelatedField()

    class Meta:
        model = Employee
        fields = "__all__"
