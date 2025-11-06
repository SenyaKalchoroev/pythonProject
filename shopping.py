from __future__ import annotations

from list_store import ListStore
from core import Product


class ShoppingCart(ListStore[Product]):
    item_type_name = "product"

    def add_product(self, name: str, qty: int = 1) -> None:
        self.add(Product(name, qty))

    def total_quantity(self) -> int:
        return sum(p.qty for p in self.all())
