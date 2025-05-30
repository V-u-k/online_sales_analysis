# product_manager.py

from product import Product 

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products:
                print(product.display_info())

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value
    
    def remove_product_by_name(self, name):
        """
        Remove a product from the inventory by its name.
        """
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Product '{name}' has been removed.")
                return
        print(f"Product '{name}' not found.")

