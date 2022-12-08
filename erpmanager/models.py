from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Unit(models.Model):
    name = models.CharField(max_length=200)
    plural_name = models.CharField(max_length=250)
    abbreviation = models.CharField(max_length=20)
    plural_abbreviation = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    hsn_sac = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    unit = models.ForeignKey(to=Unit, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        to_assign = slugify(self.name)

        if Item.objects.filter(slug=to_assign).exists():
            to_assign = to_assign + str(Item.objects.all().count())

        self.slug = to_assign

        super().save(*args, **kwargs)


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    accountnumber = models.CharField(max_length=100)
    opening_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    available_balance = models.DecimalField(max_digits=10, decimal_places=2)
    branch = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        to_assign = slugify(self.name)

        if Account.objects.filter(slug=to_assign).exists():
            to_assign = to_assign + str(Account.objects.all().count())

        self.slug = to_assign

        super().save(*args, **kwargs)


class Vendor(models.Model):
    vendorId = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        to_assign = slugify(self.name)

        if Vendor.objects.filter(slug=to_assign).exists():
            to_assign = to_assign + str(Vendor.objects.all().count())

        self.slug = to_assign

        super().save(*args, **kwargs)


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=200, null=False, blank=False, unique=True)
    firstname = models.CharField(max_length=200, null=False, blank=False)
    lastname = models.CharField(max_length=200, null=False, blank=True)
    password = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname

    def save(self, *args, **kwargs):
        to_assign = slugify(self.email)

        if Employee.objects.filter(slug=to_assign).exists():
            to_assign = to_assign + str(Employee.objects.all().count())

        self.slug = to_assign

        super().save(*args, **kwargs)


class PurchaseOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    vendorId = models.ForeignKey(to=Vendor, on_delete=models.DO_NOTHING)
    accountId = models.ForeignKey(to=Account, on_delete=models.DO_NOTHING)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class JoinPurchaseOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    vendorName=models.CharField(max_length=200)
    accountName = models.CharField(max_length=200)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class ItemTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.ForeignKey(to=Item, on_delete=models.DO_NOTHING)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchaseorderId = models.ForeignKey(to=PurchaseOrder, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# class TableColumns(models.Model):
#     id = models.IntegerField(primary_key=True)
#     columnName = models.CharField(max_length=200)
