from dataclasses import fields
from rest_framework import serializers
from .models import Account, Employee, Item, JoinPurchaseOrder, PurchaseOrder, Unit, Vendor


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = "__all__"

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        fields = "__all__"

class LogInSerializer(serializers.ModelSerializer):
        class Meta:
            model = Employee
            fields = ['email','password']

class JoinPurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinPurchaseOrder
        fields = '__all__'

# class TableColumnsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model: TableColumns
#         fields = '__all__'



