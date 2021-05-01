#########################################
# Filename: runGui.py
# Author: Roni Shternberg
# This project takes purchases data file and runs some statistics on it using simple Tkinter standard python GUI library.
# Each Purchase has 6 fields: date, time, store, category, price, and payment method (Visa, Cash, etc.)
# Notes:
# 1. The Original "purchases.txt" data file was about 200 MB, and the dates are from the year 2012.
# 2. We took the first 1000 purchases (using "head" UNIX shell command) --- about 50 KB.
# 3. We prepare the "purchases1000_new.txt" file in a script called "prepare.py"
#########################################

#########################################
# Import Statements
#########################################

from purchase_and_ledger import Purchase, Ledger

import graphs

import csv  # comma seperated values

#########################################
# Constants
#########################################

PIE_TYPE_PAYMENT = "Payment"
PIE_TYPE_CATEGORY = "Category"

########################################
# Create empty Ledger object
########################################

ledger = Ledger()

#########################################
# read purchases file into Ledger
#########################################

with open("purchases1000_new.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')  # TAB delimited
    counter = 0

    for line in csv_reader:
        if counter == 1000:
            break
        counter += 1

        # Unpack variables
        date, time, store, category, price, payment = line

        # create Purchase object
        purchase = Purchase(date, time, store, category, float(price), payment)

        # add to store list
        if store not in ledger.get_all_stores():
            ledger.add_store(store)

        # add to category list
        if category not in ledger.get_all_categories():
            ledger.add_category(category)

        # add to payment method list
        if payment not in ledger.get_all_payments():
            ledger.add_payment(payment)

        # add purchase to ledger
        ledger.add_purchase(purchase)

######################################################
# GUI Classes: MyLedgerGUI, ComboboxWindow, EntryWindow
######################################################

from tkinter import Tk, Label, Button, Toplevel, Entry, StringVar, W
from tkinter.ttk import Combobox

WINDOW_TYPE_STORE = "Store"
WINDOW_TYPE_CATEGORY = "Category"
WINDOW_TYPE_PAYMENT = "Payment"

######################################################
# MyLedgerGUI
######################################################

class MyLedgerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Ledger App")

        self.welcome_label = Label(master, text="Welcome to the U.S. Ledger of online purchases!")
        self.welcome_label.pack(side="top", fill="x")

        self.button1 = Button(master, text="1.  Print all stores.", command=self.print_all_stores)
        self.button1.pack(side="top", anchor=W)

        self.button2 = Button(master, text="2.  Print all categories.", command=self.print_all_categories)
        self.button2.pack(side="top", anchor=W)

        self.button3 = Button(master, text="3.  Print all payment methods.", command=self.print_all_payments)
        self.button3.pack(side="top", anchor=W)

        self.button4 = Button(master, text="4.  Count purchases.", command=self.count_purchases)
        self.button4.pack(side="top", anchor=W)

        self.button5 = Button(master, text="5.  Sort ledger by date (ascending).", command=self.sorting_by_date)
        self.button5.pack(side="top", anchor=W)

        self.button6 = Button(master, text="6.  Sort ledger by price (ascending).", command=self.sorting_by_price)
        self.button6.pack(side="top", anchor=W)

        self.button7 = Button(master, text="7.  Statistical summary for selected store.", command=self.stat_summary_by_store)
        self.button7.pack(side="top", anchor=W)

        self.button8 = Button(master, text="8.  Statistical summary for selected category.", command=self.stat_summary_by_category)
        self.button8.pack(side="top", anchor=W)

        self.button9 = Button(master, text="9.  Statistical summary for selected payment method.", command=self.stat_summary_by_payment)
        self.button9.pack(side="top", anchor=W)

        self.button10 = Button(master, text="10.  Total sales by stores.", command=self.total_sales_by_store)
        self.button10.pack(side="top", anchor=W)

        self.button11 = Button(master, text="11.  Total sales by categories.", command=self.total_sales_by_category)
        self.button11.pack(side="top", anchor=W)

        self.button12 = Button(master, text="12.  Total sales by payment method.", command=self.total_sales_by_payment)
        self.button12.pack(side="top", anchor=W)

        self.button13 = Button(master, text="13.  Std of sales by stores.", command=self.std_sales_by_store)
        self.button13.pack(side="top", anchor=W)

        self.button14 = Button(master, text="14. Filter Ledger by store pattern.", command=self.filter_store)
        self.button14.pack(side="top", anchor=W)
        
#         self.button15 = Button(master, text="15. Show Graphs.", command=self.show_graphs)
#         self.button15.pack(side="top", anchor=W)
        
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    ####################################
    # Handler methods
    ####################################

    # ------------------------
    def print_all_stores(self):
        ledger.print_stores()

    # ------------------------
    def print_all_categories(self):
        ledger.print_categories()

    # ------------------------
    def print_all_payments(self):
        ledger.print_payments()

    # ------------------------
    def count_purchases(self):
        print("Count of purchases in Ledger:", ledger.count_purchases())

    # ------------------------
    def sorting_by_date(self):
        ledger.sorting_by_date()

    # ------------------------
    def sorting_by_price(self):
        ledger.sorting_by_price()

    # ------------------------
    def stat_summary_by_store(self):
        newWindow = ComboboxWindow(root, ledger.get_all_stores(), WINDOW_TYPE_STORE)

        root.wait_window(newWindow)
        
        # executed only when "newWindow" is destroyed
        #print("DEBUG After waiting for window - Store")
                    
    # ------------------------
    def stat_summary_by_category(self):
        newWindow = ComboboxWindow(root, ledger.get_all_categories(), WINDOW_TYPE_CATEGORY)
        
        root.wait_window(newWindow)
        
        # executed only when "newWindow" is destroyed
        #print("DEBUG After waiting for window - Category ")

    # ------------------------
    def stat_summary_by_payment(self):
        newWindow = ComboboxWindow(root, ledger.get_all_payments(), WINDOW_TYPE_PAYMENT)

        root.wait_window(newWindow)

        # executed only when "newWindow" is destroyed
        #print("DEBUG After waiting for window - Payment ")


    # ------------------------
    def total_sales_by_store(self):
        ledger.sorting_total_sales_by_store()

    # ------------------------
    def total_sales_by_category(self):
        ledger.sorting_total_sales_by_category()
        graphs.plot_pie(PIE_TYPE_CATEGORY)
        
    # ------------------------
    def total_sales_by_payment(self):
        ledger.sorting_total_sales_by_payment()
        graphs.plot_pie(PIE_TYPE_PAYMENT)
        
    # ------------------------
    def std_sales_by_store(self):
        ledger.sorting_std_sales_by_store()

    # ------------------------
    def filter_store(self):
        newWindow = EntryWindow(root)
        
        root.wait_window(newWindow)
        
        # executed only when "newWindow" is destroyed
        #print("DEBUG After waiting for window - Filter Store ")

    # ------------------------ 
#     def show_graphs(self):
#         graphs.plot_scatter()
                   
######################################################
# ComboboxWindow
######################################################

class ComboboxWindow(Toplevel):
    def __init__(self, master, list_of_values, window_type):
        super().__init__(master=master)

        self.list_of_values = sorted(list_of_values)
        self.window_type = window_type
        
        self.title("Select " + self.window_type)
        self.geometry("390x200")

        self.label = Label(self, text="Please select " + self.window_type +": ")
        self.label.grid(column=0, row=5, padx=10, pady=25)

        # Combobox creation
        self.combo = Combobox(self, width=27, textvariable=StringVar())

        # Adding combobox drop down list
        self.combo['values'] = self.list_of_values
       
        self.combo.grid(column=1, row=5)       
        
        self.ok_button = Button(self, text="OK", command=self.ok_pressed)
        self.ok_button.grid(column=1, row=10, sticky=W, pady=4)
            
        self.combo_choice = "Nothing Selected."
        
    def ok_pressed(self):
        if self.combo.current() == -1:
            print("There is no such " + self.window_type + " in the data.")
            print("-" * 120)
            return
        
        self.combo_choice = self.list_of_values[self.combo.current()]
        
        if self.window_type == WINDOW_TYPE_STORE:
            ledger.statistics_by_store(self.combo_choice)
            
        elif self.window_type == WINDOW_TYPE_CATEGORY:
            ledger.statistics_by_category(self.combo_choice)

        elif self.window_type == WINDOW_TYPE_PAYMENT:
            ledger.statistics_by_payment(self.combo_choice)

        else: # This should never happen
            print("Illegal window type: " + self.window_type)

######################################################
# EntryWindow
######################################################

class EntryWindow(Toplevel):
    def __init__(self, master):
        super().__init__(master=master)
        
        self.title("Enter Store Pattern")
        self.geometry("390x200")     

        self.label = Label(self, text="Please enter Store pattern: ")
        self.label.grid(column=0, row=5, padx=10, pady=25)
        
        self.entry = Entry(self)       
        self.entry.grid(column=1, row=5)
        
        self.ok_button = Button(self, text="OK", command=self.ok_pressed)
        self.ok_button.grid(column=1, row=10, sticky=W, pady=4)
        
    def ok_pressed(self): 
        if self.entry.get() == "":
            print("Empty Pattern.")
            print("-" * 120)
            return
          
        ledger.filter_stores(self.entry.get());

                    
#######################
# Create and run GUI
#######################

root = Tk()
my_gui = MyLedgerGUI(root)
root.mainloop()
