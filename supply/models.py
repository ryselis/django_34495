from django.db import models


class OrderGood(models.Model):
    pass


class SupplyOrderGoodServiceBase(models.Model):
    supplier_price = models.DecimalField(max_digits=12, decimal_places=4)
    title = models.CharField(max_length=512)

    class Meta:
        ordering = ('id',)


class SupplyOrderGood(SupplyOrderGoodServiceBase):
    order_good = models.ForeignKey(to=OrderGood, on_delete=models.CASCADE)
