import unittest
from typing import List

# Product class represents a single product with its SKU, name, and price.
class Product:
    def __init__(self, sku: str, name: str, price: float):
        self.sku = sku
        self.name = name
        self.price = price

    def get_sku(self):
        return self.sku

    def get_product_info(self):
        return {
            "sku": self.sku,
            "name": self.name,
            "price": self.price
        }

# Inventory class stores the available products in the catalogue.
class Inventory:
    def __init__(self) -> None:
        self.inventory = {}

    def add_product(self, product: Product):
        # Add product to the inventory using SKU as the key.
        self.inventory[product.get_sku()] = product

    def get_inventory(self):
        return self.inventory

# PricingRule class acts as an interface for applying different discount rules.
class PricingRule:
    def apply(self, items: List[Product]) -> float:
        pass

# AppleTVRule applies the 3-for-2 deal on Apple TVs.
class AppleTVRule(PricingRule):
    def apply(self, items: List[Product]) -> float:
        atv_count = sum(1 for item in items if item.sku == 'atv')
        return -((atv_count // 3) * 109.50)  # Price of one Apple TV is deducted.

# SuperIPadRule applies bulk discount if more than 4 iPads are bought.
class SuperIPadRule(PricingRule):
    def apply(self, items: List[Product]) -> float:
        ipad_count = sum(1 for item in items if item.sku == 'ipd')
        if ipad_count > 4:
            # Bulk discount applied, price reduced from $549.99 to $499.99.
            return -(ipad_count * (549.99 - 499.99))
        return 0

# MacBookProRule provides a free VGA adapter with every MacBook Pro purchase.
class MacBookProRule(PricingRule):
    def apply(self, items: List[Product]) -> float:
        mbp_count = sum(1 for item in items if item.sku == 'mbp')
        vga_discount = -sum(30.00 for item in items if item.sku == 'vga' and mbp_count > 0)
        return vga_discount  # Free VGA adapter

# Checkout class is responsible for scanning items and calculating the total.
class Checkout:
    def __init__(self, pricing_rules: List[PricingRule], products: Inventory):
        self.pricing_rules = pricing_rules
        self.items: List[Product] = []
        self.products = products.get_inventory()

    # Adds a product to the list of scanned items based on the SKU.
    def scan(self, sku: str):
        if sku in self.products:
            self.items.append(self.products[sku])
        else:
            raise ValueError(f"Invalid SKU: {sku}")

    # Calculates the total price, applying any applicable pricing rules.
    def total(self) -> float:
        subtotal = sum(item.price for item in self.items)
        discount = sum(rule.apply(self.items) for rule in self.pricing_rules)
        return round(subtotal + discount, 2)

# Setup the inventory with the given products.
warehouse = Inventory()
warehouse.add_product(Product('ipd', 'Super iPad', 549.99))
warehouse.add_product(Product('mbp', 'MacBook Pro', 1399.99))
warehouse.add_product(Product('atv', 'Apple TV', 109.50))
warehouse.add_product(Product('vga', 'VGA adapter', 30.00))

# Create the pricing rules.
pricing_rules = [AppleTVRule(), SuperIPadRule(), MacBookProRule()]

# Unit tests for the checkout system.
class TestCheckout(unittest.TestCase):
    
    def setUp(self):
        # Initialize a new checkout instance before each test.
        self.checkout = Checkout(pricing_rules, warehouse)

    # Test for the scenario with 3 Apple TVs and 1 VGA adapter.
    def test_scenario_1(self):
        items = ['atv', 'atv', 'atv', 'vga']
        for item in items:
            self.checkout.scan(item)
        self.assertEqual(self.checkout.total(), 249.00)

    # Test for the scenario with 2 Apple TVs and 5 iPads.
    def test_scenario_2(self):
        items = ['atv', 'ipd', 'ipd', 'atv', 'ipd', 'ipd', 'ipd']
        for item in items:
            self.checkout.scan(item)
        self.assertEqual(self.checkout.total(), 2718.95)

    # Test for the scenario with 1 MacBook Pro, 1 VGA adapter, and 1 iPad.
    def test_scenario_3(self):
        items = ['mbp', 'vga', 'ipd']
        for item in items:
            self.checkout.scan(item)
        self.assertEqual(self.checkout.total(), 1949.98)

    # Test for an empty cart (no items scanned).
    def test_empty_cart(self):
        self.assertEqual(self.checkout.total(), 0.00)

    # Test invalid SKU handling (raises an exception).
    def test_invalid_sku(self):
        with self.assertRaises(ValueError):
            self.checkout.scan('xyz')  # 'xyz' is not a valid SKU.

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
