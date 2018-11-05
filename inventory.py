class Product:
    def __init__(self, product_name, price_per_unit, quantity, id=1):
        self.id = id
        self.product_name = product_name
        self.price_per_unit = price_per_unit
        self.quantity = quantity

    # get the total price of the items
    def total_product_price(self):
        total = self.price_per_unit * self.quantity
        return total

    # Return all items
    def get_items(self):
        return {
            "id": self.id,
            "product": self.product_name,
            "price": self.price_per_unit,
            "quantity": self.quantity,
            "total": self.total_product_price()
        }

# ---------------------------------------


class Inventory(Product):
    def __init__(self):
        self.id = 1
        self.inventory_store = []

    # adding each item to the inventory
    def add_to_inventory(self, product_name, price_per_unit, quantity):
        new_item = Product(product_name, price_per_unit, quantity, self.id)

        # add each item to the array of inventory_store
        self.inventory_store.append(new_item)
        self.id += 1

    # Return the total inventory value
    def get_inventory_value(self):
        return sum(
            [item.total_product_price() for item in self.inventory_store])

    # display the inventory store of all products that exist
    def display_inventory(self):
        for products in self.inventory_store:
            print(products.get_items())

        # print("-----------------")

    #Update item in inventory
    def update_product(self, selected_id, new_price, new_quantity):
      for product in self.inventory_store:
        if product.id == selected_id: 
          product.price_per_unit = new_price
          product.quantity = new_quantity

    # Delete one product in inventory
    def delete_product(self, selected_id):
      for product in self.inventory_store:
        if product.id == selected_id:
          del self.inventory_store[selected_id - 1]

    # Delete all products in inventory
    def delete_all_inventory(self):
      self.inventory_store = []
      self.id = 1
      print("Inventory has been deleted!")
      # print("-----------------")