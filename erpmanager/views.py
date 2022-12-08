from decimal import Decimal
import imp
from django.shortcuts import render
from rest_framework import generics, response, status
from .models import Account, Employee, Item, ItemTransaction, PurchaseOrder, Unit, Vendor
from .serializers import AccountSerializer, EmployeeSerializer, ItemSerializer, JoinPurchaseOrderSerializer, LogInSerializer, UnitSerializer, VendorSerializer

# Create your views here.

#Item Views
class ItemListAPIView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()

class ItemDetailAPIView(generics.GenericAPIView):
    serializer_class = ItemSerializer

    def get(self, request, slug):
        query_set = Item.objects.filter(id=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not Found', status=status.HTTP_404_NOT_FOUND)

class CreateItemAPIView(generics.CreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()   

class UpdateItemAPIView(generics.GenericAPIView):
    serializer_class = ItemSerializer

    def put(self, request, slug):
        snippet = Item.objects.filter(id=slug).first()
        serializer = ItemSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Unit Views
class UnitListAPIView(generics.ListAPIView):
    serializer_class = UnitSerializer

    def get_queryset(self):
        return Unit.objects.all()

class UnitDetailAPIView(generics.GenericAPIView):
    serializer_class = UnitSerializer

    def get(self, request, slug):
        query_set = Unit.objects.filter(id=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not Found', status=status.HTTP_404_NOT_FOUND)

class CreateUnitAPIView(generics.CreateAPIView):
    serializer_class = UnitSerializer

    def get_queryset(self):
        return Unit.objects.all()   

#Vendor views
class VendorListAPIView(generics.ListAPIView):
    serializer_class = VendorSerializer

    def get_queryset(self):
        return Vendor.objects.all()

class VendorDetailAPIView(generics.GenericAPIView):
    serializer_class = VendorSerializer

    def get(self, request, slug):
        query_set = Vendor.objects.filter(vendorId=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not Found', status=status.HTTP_404_NOT_FOUND)


#Account Views
class AccountListAPIView(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()

class AccountDetailAPIView(generics.GenericAPIView):
    serializer_class = AccountSerializer

    def get(self, request, slug):
        query_set = Account.objects.filter(id=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not Found', status=status.HTTP_404_NOT_FOUND)

class CreateAccountAPIView(generics.CreateAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()   

class UpdateAccountAPIView(generics.GenericAPIView):
    serializer_class = AccountSerializer

    def put(self, request, slug):
        snippet = Account.objects.filter(email=slug).first()
        serializer = AccountSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Employee Views
class EmployeeListAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()

class EmployeeDetailAPIView(generics.GenericAPIView):
    serializer_class = EmployeeSerializer

    def get(self, request, slug):
        query_set = Employee.objects.filter(email=slug).first()

        if query_set:
            return response.Response(self.serializer_class(query_set).data)

        return response.Response('Not Found', status=status.HTTP_404_NOT_FOUND)

class CreateEmployeeAPIView(generics.CreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.all()   

class UpdateEmployeeAPIView(generics.GenericAPIView):
    serializer_class = EmployeeSerializer

    def put(self, request, slug):
        snippet = Employee.objects.filter(email=slug).first()
        serializer = EmployeeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyLoginAPIView(generics.GenericAPIView):
        employserializer_class = EmployeeSerializer
        def get(self, request, email, password):
            snippet = Employee.objects.filter(email=email).first()
            if snippet:
                if snippet.password == password:
                    return response.Response(True)
                else:
                    return response.Response(False)
            return response.Response(False)
    

#Purchase Order views
class PurchaseOrderListAPIView(generics.ListAPIView):
    serializer_class = JoinPurchaseOrderSerializer
    def get_queryset(self):
        poData = PurchaseOrder.objects.raw('''
        Select purchaseorder.id, vendor.name as vendorName, account.name as accountName ,
        SUM(itemtransaction.amount) as total_price
        From erpmanager_purchaseorder purchaseorder 
        inner join erpmanager_vendor vendor ON vendor.vendorId = purchaseorder.vendorId_id 
        inner join erpmanager_account account ON purchaseorder.accountId_id=account.id
        inner join erpmanager_itemtransaction itemtransaction on itemtransaction.purchaseOrderId_id = purchaseorder.id''')
        return poData    

#Table Columns
# class TableColumnDetailsAPIView(generics.ListAPIView):
#     serializer_class = TableColumnsSerializer
#     def get_queryset(self, table):
#         colData = TableColumns.objects.raw('''
#         select * from INFORMATION_SCHEMA.COLUMNS
#         where TABLE_NAME="{table}"''')
#         return colData
    
