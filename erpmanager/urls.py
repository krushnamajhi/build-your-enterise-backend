from django.urls import path
from .views import AccountDetailAPIView, AccountListAPIView, CreateAccountAPIView, CreateEmployeeAPIView, CreateItemAPIView, EmployeeDetailAPIView, EmployeeListAPIView, ItemListAPIView, PurchaseOrderListAPIView, UnitDetailAPIView, CreateUnitAPIView, UnitListAPIView, UpdateAccountAPIView, UpdateEmployeeAPIView, UpdateItemAPIView, VendorDetailAPIView, VendorListAPIView, ItemDetailAPIView, VerifyLoginAPIView

urlpatterns = [
    #endpoint of Item Records
    path('items', ItemListAPIView.as_view(), name="items"),
    path('items/<str:slug>', ItemDetailAPIView.as_view(), name="item"),
    path('item/create', CreateItemAPIView.as_view(), name="item"),
    path('item/<str:slug>', UpdateItemAPIView.as_view(), name="item"),

    #endpoint of Vendor Records
    path('vendors', VendorListAPIView.as_view(), name="vendors"),
    path('vendors/<str:slug>', VendorDetailAPIView.as_view(), name="vendor"),


    #endpoints of Unit Records
    path('units', UnitListAPIView.as_view(), name="units"),
    path('units/<str:slug>', UnitDetailAPIView.as_view(), name="unit"),
    path('unit/create', CreateUnitAPIView.as_view(), name="unit"),

    #endpoint of Account Records
    path('accounts', AccountListAPIView.as_view(), name="accounts"),
    path('accounts/<str:slug>', AccountDetailAPIView.as_view(), name="account"),
    path('account/create', CreateAccountAPIView.as_view(), name="account"),
    path('account/<str:slug>', UpdateAccountAPIView.as_view(), name="account"),

    #endpoint of Item Records
    path('employees', EmployeeListAPIView.as_view(), name="employees"),
    path('employees/<str:slug>', EmployeeDetailAPIView.as_view(), name="employee"),
    path('employee/create', CreateEmployeeAPIView.as_view(), name="employee"),
    path('employee/validatelogIn/email=<str:email>&password=<str:password>', VerifyLoginAPIView.as_view(), name="employee"),

    #endpoint of Purchase order Records
    path('purchaseorders', PurchaseOrderListAPIView.as_view(), name="purchaseorder"),
    # path('purchaseorder/<str:slug>', PurchaseOrderDetailAPIView.as_view(), name="purchaseorder"),
    # path('purchaseorder/create', CreatePurchaseOrderAPIView.as_view(), name="purchaseorder"),
    # path('purchaseorder/<str:slug>', UpdatePurchaseOrderAPIView.as_view(), name="purchaseorder"),

    # path('tablecolumns', TableColumnDetailsAPIView.as_view(), name="tablecolumn"),

]
