from tkinter import *
import tkinter.ttk as ttk

# IMPORT THE INVENTORY CLASS
from inventory import Inventory

# Reusable Color Properties
_bgcolor = '#6C7A89'  # Dark Blue
_actioncolor = '#2ABB9B'
_btncolor = '#48929B'

class Inventory_Screen(Inventory):
    def __init__(self, window):
        Inventory.__init__(self)

        # Window used within screen and main app window
        self.window = None
        self.main_window = window

    def display_inventory_items(self):
        self.new_screen("All Inventory Items", "600x400")
        self.all_items_list()

        for products in self.inventory_store:
            # Grabs all items added to inventory
            products.get_items()

            # Creates String to display on list
            display_text = "ID: {}  Product Name: {}  Price: {}  Quantity: {}  Total Price: {}".format(
                products.id, products.product_name, products.price_per_unit, products.quantity, products.total_product_price()
            )

            # Adds all items to list to display
            self.Items_list.insert(products.id, display_text)

            
    def all_items_list(self):
        self.Items_list = Listbox(self.window)
        self.Items_list.place(relx=0.033, rely=0.067, relheight=0.889 , relwidth=0.935)
        self.Items_list.configure(background="white")
        self.Items_list.configure(font="TkFixedFont")
        self.Items_list.configure(width=560)

    def new_item(self):
        self.new_screen("New Item")
        self.new_item_menu()

    # Updating an item
    def update_item(self):
        self.new_screen("Update Item")
        self.update_item_menu()

    def update_item_menu(self):
        self.Entry0 = Entry(self.window)
        self.Entry0.place(relx=0.33, rely=0.133,height=20, relwidth=0.35)
        self.Entry0.configure(background="white")
        self.Entry0.configure(font="TkFixedFont")

        self.Label0 = Label(self.window)
        self.Label0.place(relx=0.40, rely=0.067, height=18, width=90)
        self.Label0.configure(text='''Product ID''')

        self.Label2 = Label(self.window)
        self.Label2.place(relx=0.40, rely=0.244, height=18, width=85)
        self.Label2.configure(text='''Price per unit''')

        self.Entry2 = Entry(self.window)
        self.Entry2.place(relx=0.33, rely=0.311,height=20, relwidth=0.35)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        self.Label3 = Label(self.window)
        self.Label3.place(relx=0.43, rely=0.422, height=18, width=56)
        self.Label3.configure(text='''Quantity''')

        self.Entry3 = Entry(self.window)
        self.Entry3.place(relx=0.33, rely=0.489,height=20, relwidth=0.35)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")

        self.Button1 = Button(self.window)
        self.Button1.place(relx=0.36, rely=0.689, height=26, width=120)
        self.Button1.configure(activebackground=_actioncolor)
        self.Button1.configure(background=_btncolor)
        self.Button1.configure(command=self.done_update)
        self.Button1.configure(text='''Done''')

    def done_update(self):
        return self.done(False)

    def done(self,add_item = True):
        # Data    
        # product_name = self.Entry1.get()
        price_per_unit = int(self.Entry2.get())
        quantity = int(self.Entry3.get())

        if add_item:
        # Creates new item into inventory with input
            product_name = self.Entry1.get()
            self.add_to_inventory(product_name, price_per_unit, quantity)
        else:
            id = int(self.Entry0.get())
            self.update_product(id, price_per_unit, quantity)
    
        # Closes the window after done
        self.window.destroy()


    # Delete one product item
    def delete_item(self):
        self.new_screen("Delete Item")
        self.delete_item_menu()

    def delete_item_menu(self):
        self.Entry0 = Entry(self.window)
        self.Entry0.place(relx=0.33, rely=0.133,height=20, relwidth=0.35)
        self.Entry0.configure(background="white")
        self.Entry0.configure(font="TkFixedFont")

        self.Label0 = Label(self.window)
        self.Label0.place(relx=0.40, rely=0.067, height=18, width=90)
        self.Label0.configure(text='''Product ID''')

        self.Button1 = Button(self.window)
        self.Button1.place(relx=0.36, rely=0.689, height=26, width=120)
        self.Button1.configure(activebackground=_actioncolor)
        self.Button1.configure(background=_btncolor)
        self.Button1.configure(command=self.delete)
        self.Button1.configure(text='''Delete''')

    # -------------------------

    def delete(self, delete_one_item=True):
        id = int(self.Entry0.get())
        if delete_one_item:
            self.delete_product(id)
        else:
            self.delete_all_inventory()

        # Closes the window after done
        self.window.destroy()

    # -------------------------



    # Closes the main Window
    def quit(self):
        self.main_window.destroy()

    def new_screen(self, title, size="400x400"):
        self.window = Toplevel()
        self.window.geometry(size)
        self.window.title(title)
        self.window.config(background=_bgcolor)

    def new_item_menu(self):
        self.Entry1 = Entry(self.window)
        self.Entry1.place(relx=0.33, rely=0.133,height=20, relwidth=0.35)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Label1 = Label(self.window)
        self.Label1.place(relx=0.40, rely=0.067, height=18, width=90)
        self.Label1.configure(text='''Product Name''')

        self.Label2 = Label(self.window)
        self.Label2.place(relx=0.40, rely=0.244, height=18, width=85)
        self.Label2.configure(text='''Price per unit''')

        self.Entry2 = Entry(self.window)
        self.Entry2.place(relx=0.33, rely=0.311,height=20, relwidth=0.35)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        self.Label3 = Label(self.window)
        self.Label3.place(relx=0.43, rely=0.422, height=18, width=56)
        self.Label3.configure(text='''Quantity''')

        self.Entry3 = Entry(self.window)
        self.Entry3.place(relx=0.33, rely=0.489,height=20, relwidth=0.35)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")

        self.Button1 = Button(self.window)
        self.Button1.place(relx=0.36, rely=0.689, height=26, width=120)
        self.Button1.configure(activebackground=_actioncolor)
        self.Button1.configure(background=_btncolor)
        self.Button1.configure(command=self.done)
        self.Button1.configure(text='''Done''')

class GUI:
    def __init__(self, top=None):


        # Initial GUI Configuration
        top.geometry("600x450+650+122")
        top.configure(background=_bgcolor)
        top.title("Inventory")

        # Inventory Screen Instance
        inventory_screen = Inventory_Screen(top)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.25, rely=0.111)
        self.Label1.config(font=("Courier", 20))
        self.Label1.configure(text='''Welcome To Inventory''')

        self.Button1 = Button(top)
        self.Button1.place(relx=0.433, rely=0.233, height=26, width=120)
        self.Button1.configure(background=_btncolor)
        self.Button1.configure(activebackground=_actioncolor)
        self.Button1.configure(command=inventory_screen.new_item)
        self.Button1.configure(text='''New Product''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.433, rely=0.355, height=26, width=120)
        self.Button2.configure(background=_btncolor)
        self.Button2.configure(activebackground=_actioncolor)
        self.Button2.configure(command=inventory_screen.display_inventory_items)
        self.Button2.configure(text='''View Inventory''')

        self.Button3 = Button(top)
        self.Button3.place(relx=0.433, rely=0.477, height=26, width=120)
        self.Button3.configure(background=_btncolor)
        self.Button3.configure(activebackground=_actioncolor)
        self.Button3.configure(command=inventory_screen.update_item)
        self.Button3.configure(text='''Update a Product''')

        self.Button4 = Button(top)
        self.Button4.place(relx=0.433, rely=0.599, height=26, width=120)
        self.Button4.configure(background=_btncolor)
        self.Button4.configure(activebackground=_actioncolor)
        self.Button4.configure(command=inventory_screen.delete_item)
        self.Button4.configure(text='''Delete a Product''')

        self.Button5 = Button(top)
        self.Button5.place(relx=0.433, rely=0.721, height=26, width=120)
        self.Button5.configure(background=_btncolor)
        self.Button5.configure(activebackground=_actioncolor)
        self.Button5.configure(command=inventory_screen.display_inventory_items)
        self.Button5.configure(text='''Delete Inventory''')

        self.Button6 = Button(top)
        self.Button6.place(relx=0.433, rely=0.844, height=26, width=120)
        self.Button6.configure(background=_btncolor)
        self.Button6.configure(activebackground=_actioncolor)
        self.Button6.configure(command=inventory_screen.quit)
        self.Button6.configure(text='''Quit''')

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    root = Tk()
    GUI(root)
    root.mainloop()

if __name__ == '__main__':
    vp_start_gui()