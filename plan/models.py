from django.db import models

# Create your models here.

class Merchant(models.Model):
    merchant_name = models.CharField("Merchant Name", max_length=20)

    def __str__(self):
        return self.merchant_name    


class Store(models.Model):
    store_name = models.CharField("Store Name", max_length=30)
    store_address = models.CharField("Store Address", max_length=50)
    s_latitude = models.FloatField("Latitude", blank=True, null=True)
    s_longitude = models.FloatField("Longitude", blank=True, null=True)
    merchant = models.ForeignKey(Merchant, related_name="merchant_stores", on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.store_name, self.merchant)  

    def save(self, *args, **kwargs):
        if not self.store_name[0].isupper():
            pass
        super(Store, self).save(*args, **kwargs)     


class Item(models.Model):
    item_name = models.CharField("Item Name", max_length=300)
    item_price = models.FloatField("Item Price", default=0)
    item_description = models.TextField("Item Description", blank=True)
    merchant = models.ForeignKey(Merchant, related_name="merchant_items", on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.item_name, self.item_price)   


class Transaction(models.Model):
    store = models.ForeignKey(Store, related_name="store_transactions", on_delete=models.CASCADE)
    merchant = models.ForeignKey(Merchant, related_name="merchant_transactions", on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name="tx_items")

    def __str__(self):
        return "{}-{}".format(self.pk, self.store, self.merchant)