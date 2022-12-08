from django.contrib import admin
from .models import Account, Employee, Item, ItemTransaction, PurchaseOrder, Unit, Vendor


class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields= ('name','hsn_sac')
    list_per_page=2

class VendorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at','address','city','state')
    search_fields= ('name','city','state')
    list_per_page=2

# Register your models here.


admin.site.register(Item, ItemModelAdmin)
admin.site.register(Unit)
admin.site.register(Vendor, VendorModelAdmin)
admin.site.register(Account)
admin.site.register(Employee)
admin.site.register(PurchaseOrder)
admin.site.register(ItemTransaction)

