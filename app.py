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

        for items in self.inventory_store:
            # Grabs all items added to inventory
            id, product_name, price, quantity, total_price = items.get_items()

            # Creates String to display on list
            display_text = "ID: {}  Product Name: {}  Price: {}  Quantity: {}  Total Price: {}".format(
                id, product_name, price, quantity, total_price
            )

            # Adds all items to list to display
            self.Items_list.insert(id, display_text)
            
    def all_items_list(self):
        self.Items_list = Listbox(self.window)
        self.Items_list.place(relx=0.033, rely=0.067, relheight=0.889 , relwidth=0.935)
        self.Items_list.configure(background="white")
        self.Items_list.configure(font="TkFixedFont")
        self.Items_list.configure(width=560)

    def new_item(self):
        self.new_screen("New Item")
        self.new_item_menu()

    def done(self):
        # Data    
        produc_name = self.Entry1.get()
        price = int(self.Entry2.get())
        quantity = int(self.Entry3.get())

        # Creates new item into inventory with input
        self.add_to_inventory(produc_name, price, quantity)

        # Closes the window after done
        self.window.destroy()

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
        self.Entry1.place(relx=0.343, rely=0.133,height=20, relwidth=0.35)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")

        self.Label1 = Label(self.window)
        self.Label1.place(relx=0.40, rely=0.067, height=18, width=90)
        self.Label1.configure(text='''Product Name''')

        self.Label2 = Label(self.window)
        self.Label2.place(relx=0.40, rely=0.244, height=18, width=85)
        self.Label2.configure(text='''Price per unit''')

        self.Entry2 = Entry(self.window)
        self.Entry2.place(relx=0.383, rely=0.311,height=20, relwidth=0.243)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        self.Label3 = Label(self.window)
        self.Label3.place(relx=0.43, rely=0.422, height=18, width=56)
        self.Label3.configure(text='''Quantity''')

        self.Entry3 = Entry(self.window)
        self.Entry3.place(relx=0.383, rely=0.489,height=20, relwidth=0.243)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")

        self.Button1 = Button(self.window)
        self.Button1.place(relx=0.425, rely=0.689, height=26, width=57)
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
        self.Button1.place(relx=0.433, rely=0.244, height=26, width=84)
        self.Button1.configure(background=_btncolor)
        self.Button1.configure(activebackground=_actioncolor)
        self.Button1.configure(command=inventory_screen.new_item)
        self.Button1.configure(text='''New Item''')

        self.Button2 = Button(top)
        self.Button2.place(relx=0.433, rely=0.422, height=26, width=84)
        self.Button2.configure(background=_btncolor)
        self.Button2.configure(activebackground=_actioncolor)
        self.Button2.configure(command=inventory_screen.display_inventory_items)
        self.Button2.configure(text='''Inventory''')

        self.Button3 = Button(top)
        self.Button3.place(relx=0.467, rely=0.644, height=26, width=51)
        self.Button3.configure(background=_btncolor)
        self.Button3.configure(activebackground=_actioncolor)
        self.Button3.configure(command=inventory_screen.quit)
        self.Button3.configure(text='''Quit''')

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    root = Tk()
    GUI(root)
    root.mainloop()

if __name__ == '__main__':
    vp_start_gui()