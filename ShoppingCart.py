class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product_id, product_name, quantity, unit_price):
        product = {
            "id": product_id,
            "name": product_name,
            "quantity": quantity,
            "unit_price": unit_price
        }
        self.cart.append(product)

    def remove_from_cart(self, product_id, quantity_to_remove=0):
        for product in self.cart:
            if product["id"] == product_id:
                product["quantity"]=product["quantity"]-quantity_to_remove
            if product["quantity"]==0 or product["quantity"]<0:
                self.cart.remove(product)
            
            
    def display_cart(self):
        if self.cart:
            print("Shopping Cart Contents:")
            for product in self.cart:
                total_price = product['quantity'] * product['unit_price']
                print(f"ID: {product['id']}, Name: {product['name']}, Quantity: {product['quantity']}, Unit Price: {product['unit_price']}, Total Price: {total_price}")
        else:
            print("Your shopping cart is empty.")




