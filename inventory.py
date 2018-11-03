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

    # print properties one by one here
    def display_item_details(self):
      item_details: {
        "id": self.id,
        "product name": self.product_name,
        "price per unit": self.price_per_unit,
        "quantity": self.quantity,
        "product total": self.total_price()
      }

      self.id += 1


# ---------------------------------------


class Inventory(Item):
  def __init__(self):
    self.id = 1
    self.inventory_store = []

  # adding each item to the inventory
  def add_to_inventory(self, product_name, price_per_unit, quantity):
    Item(id, product_name, price_per_unit, quantity)

    # have a loop to display all the items
    

    # add each item to the array of inventory_store
    self.inventory_store.append(item_details)
    self.id += 1
  
  # display the inventory store of all items that exist
  def display_inventory(self):
    print(self.inventory_store)



# ----------------------------------------------
# Inputs

inventory = Inventory()
inventory.add_to_inventory("starbursts", 2, 5)
inventory.add_to_inventory("whoopers", 4, 6)
inventory.add_to_inventory("donuts", 2, 3)
inventory.add_to_inventory("adidas socks", 9, 13)
inventory.add_to_inventory("adidas kids shoes", 120, 11)

# displaying inventory

inventory.display_inventory()

