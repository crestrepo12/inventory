class Item:
    def __init__(self, product_name, price_per_unit, quantity, id = 1):
        self.id = id
        self.product_name = product_name
        self.price_per_unit = price_per_unit
        self.quantity = quantity

    # get the total price of the items
    def total_price(self):
        total = self.price_per_unit * self.quantity
        return total

    # Return all items
    def get_items(self):
        return (self.id, self.product_name,
               self.price_per_unit, self.quantity,
               self.total_price())

# ---------------------------------------

class Inventory(Item):
  def __init__(self):
    self.id = 1
    self.inventory_store = []

  # adding each item to the inventory
  def add_to_inventory(self, product_name, price_per_unit, quantity):
    new_item = Item(product_name, price_per_unit, quantity, self.id)

    # add each item to the array of inventory_store
    self.inventory_store.append(new_item)
    self.id += 1

  # Return the total inventory value
  def get_inventory_value(self):
    return sum([item.total_price() for item in self.inventory_store]) 
  
  # display the inventory store of all items that exist
  def display_inventory(self):
    for products in self.inventory_store:
      id, product, price, quantity, total = products.get_items()
      print("ID: {} | Product: {} | Price: {} | Quantity: {} | Total {}".format(
        id, product, price, quantity, total
      ))

# # ----------------------------------------------
# # Inputs

# inventory = Inventory()
# inventory.add_to_inventory("starbursts", 2, 5)
# inventory.add_to_inventory("whoopers", 4, 6)
# inventory.add_to_inventory("donuts", 2, 3)
# inventory.add_to_inventory("adidas socks", 9, 13)
# inventory.add_to_inventory("adidas kids shoes", 120, 11)

# # displaying inventory

# inventory.display_inventory()
# print(inventory.get_inventory_value())