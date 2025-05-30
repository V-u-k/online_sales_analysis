# cart.py

from product import Product

class Cart:
    def __init__(self):
        # List of items in the cart
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        """
        Add a product to the cart if enough stock is available.
        """
        if quantity <= product.quantity:
            self.cart_items.append({"product": product, "quantity": quantity})
            product.update_quantity(-quantity)
        else:
            print(f"Not enough stock for {product.name}. Available: {product.quantity}")

    def calculate_total(self):
        """
        Calculate the total value of the cart.
        """
        total = sum(item["product"].price * item["quantity"] for item in self.cart_items)
        return total

    def display_cart(self):
        """
        Display the contents of the cart.
        """
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Cart Contents:")
            for item in self.cart_items:
                product = item["product"]
                quantity = item["quantity"]
                print(f"{product.name} - {quantity} pcs - ${product.price * quantity:.2f}")
