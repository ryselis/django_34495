from decimal import Decimal

from django.test import TestCase

from supply.models import OrderGood, SupplyOrderGood


class Ticket34495TestCase(TestCase):
    def setUp(self) -> None:
        self.order_good = OrderGood.objects.create()
        self.supply_order_good = SupplyOrderGood.objects.create(order_good=self.order_good,
                                                                supplier_price=Decimal(5),
                                                                title='Glass')

    def test_update_supplier_price_works(self):
        SupplyOrderGood.objects.filter(order_good_id=self.order_good.pk).update(supplier_price=Decimal(6))
        self.supply_order_good.refresh_from_db()
        self.assertEqual(Decimal(6), self.supply_order_good.supplier_price)
