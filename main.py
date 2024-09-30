from typing import Dict, List

# Product class representing individual items in inventory
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

# Inventory class to manage the list of available products
class Inventory:
    def __init__(self) -> None:
        self.inventory = dict()

    def add_product(self, product: Product):
        self.inventory[product.get_sku()] = product

    def get_inventory(self):
        return self.inventory

# Abstract PricingRule class that all pricing rules inherit from
class PricingRule:
    def apply(self, items: List[Product]) -> float:
        pass

# Apple TV pricing rule (3 for the price of 2)
class AppleTVRule(PricingRule):
    def apply(self, items: List[Product]) -> float:
        atv_count = sum(1 for item in items if item.sku == 'atv')
        return -((atv_count // 3) * 109.50)  # Price of one Apple TV

# Super iPad bulk discount pricing rule
class SuperIPadRule(PricingRule):
    def apply(self, items: List[Product]) -> float:
        ipad_count = sum(1 for item in items if item.sku == 'ipd')
        if ipad_count > 4:
            return -(ipad_count * (549.99 - 499.99))  # Discount of $50 per iPad
        return 0

# MacBook Pro pricing rule (free VGA adapter with every MacBook Pro)
class MacBookProRule(PricingRule):
    def apply(self, items: List[Product]) -> float:
        mbp_count = sum(1 for item in items if item.sku == 'mbp')
        vga_price = 30.00
        return -(mbp_count * vga_price)  # Free VGA adapter with each MacBook Pro

# Checkout class to handle scanning and calculating total price
class Checkout:
    def __init__(self, pricing_rules: List[PricingRule], products: Inventory):
        self.pricing_rules = pricing_rules
        self.items: List[Product] = []
        self.products = products.get_inventory()

    def scan(self, sku: str):
        if sku in self.products:
            self.items.append(self.products[sku])
        else:
            raise ValueError(f"Invalid SKU: {sku}")

    def total(self) -> float:
        subtotal = sum(item.price for item in self.items)
        discount = sum(rule.apply(self.items) for rule in self.pricing_rules)
        return round(subtotal + discount, 2)


# Initialize Inventory with products
warehouse = Inventory()
warehouse.add_product(Product('ipd', 'Super iPad', 549.99))
warehouse.add_product(Product('mbp', 'MacBook Pro', 1399.99))
warehouse.add_product(Product('atv', 'Apple TV', 109.50))
warehouse.add_product(Product('vga', 'VGA adapter', 30.00))

# Pricing rules for opening day specials
pricing_rules = [AppleTVRule(), SuperIPadRule(), MacBookProRule()]

# Sample function to simulate test scenarios
def run_scenario(skus):
    checkout = Checkout(pricing_rules, warehouse)
    for sku in skus:
        checkout.scan(sku)
    return checkout.total()


# Uncomment the following lines to run test scenarios
print(f"Total for scenario 1: ${run_scenario(['atv', 'atv', 'atv', 'vga'])}")
print(f"Total for scenario 2: ${run_scenario(['atv', 'ipd', 'ipd', 'atv', 'ipd', 'ipd', 'ipd'])}")
print(f"Total for scenario 3: ${run_scenario(['mbp', 'vga', 'ipd'])}")
