import unittest
from main import Checkout, Product, Inventory, AppleTVRule, SuperIPadRule, MacBookProRule

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        # Set up inventory
        self.inventory = Inventory()
        self.inventory.add_product(Product('ipd', 'Super iPad', 549.99))
        self.inventory.add_product(Product('mbp', 'MacBook Pro', 1399.99))
        self.inventory.add_product(Product('atv', 'Apple TV', 109.50))
        self.inventory.add_product(Product('vga', 'VGA adapter', 30.00))
        
        # Pricing rules
        self.pricing_rules = [AppleTVRule(), SuperIPadRule(), MacBookProRule()]

    def test_scenario_1(self):
        checkout = Checkout(self.pricing_rules, self.inventory)
        checkout.scan('atv')
        checkout.scan('atv')
        checkout.scan('atv')
        checkout.scan('vga')
        self.assertEqual(checkout.total(), 249.00)

    def test_scenario_2(self):
        checkout = Checkout(self.pricing_rules, self.inventory)
        checkout.scan('atv')
        checkout.scan('ipd')
        checkout.scan('ipd')
        checkout.scan('atv')
        checkout.scan('ipd')
        checkout.scan('ipd')
        checkout.scan('ipd')
        self.assertEqual(checkout.total(), 2718.95)

    def test_scenario_3(self):
        checkout = Checkout(self.pricing_rules, self.inventory)
        checkout.scan('mbp')
        checkout.scan('vga')
        checkout.scan('ipd')
        self.assertEqual(checkout.total(), 1949.98)

    def test_invalid_sku(self):
        checkout = Checkout(self.pricing_rules, self.inventory)
        with self.assertRaises(ValueError):
            checkout.scan('invalid_sku')

if __name__ == '__main__':
    unittest.main()
