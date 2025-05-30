# main.py

from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def main():
    manager = ProductManager()

    # Add products to inventory(changed names and quantities)
    manager.add_product(Product("Tablet", 1200.99, 7))
    manager.add_product(Product("Printer", 25.50, 12))
    manager.add_product(Product("Keyboard", 45.00, 10))
    manager.add_product(Product("Monitor", 250.75, 7))

    #print("All products:")
    #manager.display_all_products()

<<<<<<< HEAD
    #print(f"\nTotal inventory value: ${manager.total_inventory_value():.2f}")
=======
    # Print total inventory value
    print(f"\nTotal inventory value: ${manager.total_inventory_value():.2f}")
>>>>>>> add-cart-functionality

    # Create an instance of Cart
    cart = Cart()

    # Add three randomly selected products to the cart
    available_products = manager.products
    for _ in range(3):
        product = random.choice(available_products)
        max_quantity = min(product.quantity, 3)
        if max_quantity > 0:
            quantity = random.randint(1, max_quantity)
            cart.add_to_cart(product, quantity)

    # Display cart contents and total value
    print("\nCart contents:")
    cart.display_cart()
    print(f"\nTotal cart value: ${cart.calculate_total():.2f}")

if __name__ == "__main__":
    main()
