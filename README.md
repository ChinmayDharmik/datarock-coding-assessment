# DataRock Checkout System

## Overview

This project is a solution for the DataRock test, where we were tasked with building a checkout system for a new computer store. The system allows for flexible pricing rules that can change as needed. The checkout system can scan items in any order, apply discounts, and calculate the total.

The following products are in the store's catalogue:

| SKU     | Name        | Price    |
| ------- | ----------- | --------:|
| ipd     | Super iPad  | $549.99  |
| mbp     | MacBook Pro | $1399.99 |
| atv     | Apple TV    | $109.50  |
| vga     | VGA adapter | $30.00   |

### Opening Day Specials
1. **3-for-2 deal on Apple TVs**: Buy 3 Apple TVs and only pay for 2.
2. **Bulk discount on Super iPads**: If more than 4 iPads are purchased, the price drops from $549.99 to $499.99 each.
3. **Free VGA adapter with every MacBook Pro**: Every MacBook Pro purchase comes with a free VGA adapter.

The checkout system allows flexible pricing rules that can be modified for future promotions.

## Requirements

### Languages
- **Python** was used for this implementation.

### Key Features
- **Flexible Pricing Rules**: The pricing rules can be easily modified or extended as new promotions are introduced.
- **Scans Items in Any Order**: The checkout system is able to scan items in any order, and pricing rules are applied when the total is calculated.
- **Exception Handling for Invalid SKUs**: The system will raise a `ValueError` if an invalid SKU is scanned.

## Setup and Usage

### 1. Clone the Repository
```bash
git clone <repository-url>
cd DataRock-checkout
```

### 2. Run the Code

You can run the checkout scenarios directly by executing the Python script, which includes predefined test scenarios.

```bash
python main.py
```

### 3. Unit Tests

Unit tests have been included to verify the correct behavior of the checkout system. The tests cover multiple scenarios as outlined in the problem description.

To run the unit tests, execute the following command:
```bash
python -m unittest main.py
```

## Example Scenarios

- **Scenario 1**: SKUs Scanned: `atv`, `atv`, `atv`, `vga`
  - Total expected: $249.00
- **Scenario 2**: SKUs Scanned: `atv`, `ipd`, `ipd`, `atv`, `ipd`, `ipd`, `ipd`
  - Total expected: $2718.95
- **Scenario 3**: SKUs Scanned: `mbp`, `vga`, `ipd`
  - Total expected: $1949.98

## Code Structure

### Key Classes

1. **`Product`**: Represents an individual product in the store with SKU, name, and price.
2. **`Inventory`**: Manages the list of available products in the store's catalogue.
3. **`PricingRule`**: Base class for implementing various pricing rules. Subclasses include:
   - **`AppleTVRule`**: Implements the 3-for-2 deal for Apple TVs.
   - **`SuperIPadRule`**: Implements bulk discount for Super iPads.
   - **`MacBookProRule`**: Provides a free VGA adapter with each MacBook Pro.
4. **`Checkout`**: Handles scanning items and applying pricing rules to calculate the total.

### Key Methods

- **`scan(sku: str)`**: Adds the product identified by the SKU to the checkout.
- **`total()`**: Applies all relevant pricing rules and calculates the final total.

### Tests

The system includes unit tests for the following scenarios:
- Scenario 1: Multiple Apple TVs and a VGA adapter.
- Scenario 2: Multiple iPads, Apple TVs, and bulk discount rules.
- Scenario 3: Combination of MacBook Pro, iPad, and VGA adapter.
