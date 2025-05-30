# online_sales_analysis
Repo for Assignment - Final Project
# README.md

## Online Sales Analysis

This project is a simple Python application for managing products and simulating a shopping cart system.

### Project Structure

- **product.py**  
  Contains the `Product` class, which represents a product with a name, price, and quantity.  
  - Methods:  
    - `display_info()`: Returns product details as a string.  
    - `update_quantity(amount)`: Updates the product quantity.

- **product_manager.py**  
  Contains the `ProductManager` class, which manages a list of products.  
  - Methods:  
    - `add_product(product)`: Adds a product to the inventory.  
    - `display_all_products()`: Prints all products.  
    - `total_inventory_value()`: Calculates the total value of all products.  
    - `remove_product_by_name(name)`: Removes a product by its name.

- **cart.py**  
  Contains the `Cart` class, which manages the shopping cart.  
  - Methods:  
    - `add_to_cart(product, quantity)`: Adds a product to the cart if enough stock is available.  
    - `calculate_total()`: Calculates the total value of the cart.  
    - `display_cart()`: Displays the contents of the cart.

- **main.py**  
  The main script that demonstrates adding products, creating a cart, adding random products to the cart, and displaying the cart contents and total value.

### Functionality

- Add and manage products in inventory.
- Remove products by name.
- Simulate a shopping cart: add products, view cart, and calculate total price.
- Sensitive data (like `config.json`) and screenshots (`*.png`) are ignored by git.
