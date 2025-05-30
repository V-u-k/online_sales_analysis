# main.py

from product import Product
from product_manager import ProductManager

def main():
    manager = ProductManager()

    # Add products to inventory(changed names and quantities)
    manager.add_product(Product("Tablet", 1200.99, 7))
    manager.add_product(Product("Printer", 25.50, 12))
    manager.add_product(Product("Keyboard", 45.00, 10))
    manager.add_product(Product("Monitor", 250.75, 7))

    #print("All products:")
    #manager.display_all_products()

    #print(f"\nTotal inventory value: ${manager.total_inventory_value():.2f}")

if __name__ == "__main__":
    main()
