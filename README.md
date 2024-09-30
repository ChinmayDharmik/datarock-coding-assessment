# DataRock Checkout System

### Overview

This project implements a checkout system for **Datarock Computer Store**, which includes a flexible pricing system to accommodate opening day specials and any future promotional rules. The checkout system scans items and calculates the total price while applying special discounts and deals.

The system has been developed using **Python**, with unit tests included for key scenarios.

### Products in the Catalogue

The following products are available in the store's catalogue:

| SKU  | Name        | Price   |
|------|-------------|---------|
| ipd  | Super iPad  | $549.99 |
| mbp  | MacBook Pro | $1399.99|
| atv  | Apple TV    | $109.50 |
| vga  | VGA Adapter | $30.00  |

### Opening Day Special Pricing Rules

1. **Apple TV Offer**: Buy 3 Apple TVs for the price of 2.
2. **Super iPad Bulk Discount**: If more than 4 Super iPads are purchased, the price drops to $499.99 per unit.
3. **MacBook Pro Offer**: Every MacBook Pro purchase includes a free VGA adapter.

### Installation and Setup

To set up and run this checkout system, follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ChinmayDharmik/datarock-coding-assessment.git
   cd datarock-coding-assessment
   ```

2. **Install Python (if not already installed)**:
   Ensure that you have Python 3.x installed on your machine.

3. **Run the Tests**:
   Run the provided unit tests to ensure everything is set up correctly.
   ```bash
   python -m unittest test.py
   ```

4. **Running the Script**:
   You can run custom checkout scenarios by modifying the scenarios in the `run_scenario()` function in the main Python script or adding new ones to the unit tests.

### Code Structure

- `Product`: Class representing a single product, holding its SKU, name, and price.
- `Inventory`: Class managing the available products in the inventory.
- `PricingRule`: Abstract class representing the interface for various pricing rules.
- `AppleTVRule`: Pricing rule for applying the "Buy 3 for the price of 2" Apple TV deal.
- `SuperIPadRule`: Pricing rule for applying bulk discounts for Super iPads.
- `MacBookProRule`: Pricing rule for bundling free VGA adapters with MacBook Pro purchases.
- `Checkout`: Main class responsible for scanning items, calculating the total, and applying the pricing rules.

### Example Scenarios

Here are some example scenarios and the expected results:

1. **Scenario 1**: Three Apple TVs and a VGA Adapter.
   ```bash
   SKUs Scanned: atv, atv, atv, vga
   Total Expected: $249.00
   ```

2. **Scenario 2**: Two Apple TVs and five Super iPads.
   ```bash
   SKUs Scanned: atv, ipd, ipd, atv, ipd, ipd, ipd
   Total Expected: $2718.95
   ```

3. **Scenario 3**: One MacBook Pro, one VGA Adapter, and one Super iPad.
   ```bash
   SKUs Scanned: mbp, vga, ipd
   Total Expected: $1949.98
   ```

### Running Tests

Unit tests are provided to verify the accuracy of the checkout system. To run the tests:

```bash
python -m unittest test.py
```

These tests cover various scenarios to ensure that the pricing rules are applied correctly and that the checkout system behaves as expected.

### Pricing Flexibility

This checkout system is designed to be flexible. You can easily add or modify pricing rules by creating new classes that extend the `PricingRule` interface, ensuring that the system can adapt to future changes in pricing and promotions with minimal effort.

### Future Improvements

- **Additional Pricing Rules**: Support for more complex promotions (e.g., percentage discounts, combo offers).
- **Database Integration**: Instead of using an in-memory inventory, integrate a database to handle larger inventories.
- **Command Line Interface**: Build a simple command-line interface for easier interaction with the checkout system.


Thank you for reviewing this submission for the **DataRock Checkout System** test.