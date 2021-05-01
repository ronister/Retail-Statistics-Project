#########################################
# Filename: run.py
# Author: Roni Shternberg
# This project takes purchases data file and runs some statistics on it.
# Each Purchase has 6 fields: date, time, store, category, price, and payment method (Visa, Cash, etc.)
# Notes:
# 1. The Original "purchases.txt" data file was about 200 MB, and the dates are from the year 2012.
# 2. We took the first 1000 purchases (using "head" UNIX shell command) --- about 50 KB.
# 3. We prepare the "purchases1000_new.txt" file in a script called "prepare.py"
#########################################

#########################################
# Import Statements
#########################################

import csv  # comma seperated values
import re  # regular expressions

#########################################
# Class definitions
#########################################

class Purchase:

    def __init__(self, date, time, store, category, price, payment):
        self.date = date
        self.time = time
        self.store = store
        self.category = category
        self.price = price
        self.payment = payment

class Ledger:  # account book, record book - "a book or other collection of financial accounts of a particular type."

    def __init__(self):
        self.purchases_list = []  # list of purchase objects
        self.stores_list = []  # list of names of different stores
        self.categories_list = []  # list of names of unique categories

    # get list of stores
    def get_all_stores(self):
        return self.stores_list

    # get list of categories
    def get_all_categories(self):
        return self.categories_list

    # add to list of purchases
    def add_purchase(self, purchase):
        self.purchases_list.append(purchase)

    # add to list of stores
    def add_store(self, store):
        self.stores_list.append(store)

    # add to list of categories
    def add_category(self, category):
        self.categories_list.append(category)

    # count number of purchases
    def count_purchases(self):
        return len(self.purchases_list)

    # get purchase at index i
    def get_purchase_at(self, i):
        return self.purchases_list[i]

    # ---------------------------------------------------------------------------
    # print list of ledger
    def print_ledger(self):
        print("{:<10}        {:<9}  {:<15}   {:<25}  {:<15}  {:<20}".format("Date"
                                                                            , "Time", "Store", "Category", "Price",
                                                                            "Payment"))
        for purchase in self.purchases_list:
            print("{}        {}      {:<15}   {:<25}  {:<15}  {:<20}".format(purchase.date
                                                                             , purchase.time, purchase.store,
                                                                             purchase.category, purchase.price,
                                                                             purchase.payment))
        print("-" * 100)

    # ---------------------------------------------------------------------------
    # print list of stores
    def print_stores(self):
        self.stores_list = sorted(self.stores_list)
        for store in self.stores_list:
            print(store)
        print("Total of", len(self.stores_list), "different stores.")
        print("-" * 100)
    # ---------------------------------------------------------------------------

    # print list of categories
    def print_categories(self):
        self.categories_list = sorted(self.categories_list)
        for category in self.categories_list:
            print(category)
        print("Total of", len(self.categories_list), "unique categories.")
        print("-" * 100)
    # --------------------------------------------------------------------------------

    # sorting list by date
    def sorting_by_date(self, reverse = False):
        self.purchases_list = sorted(self.purchases_list, key=lambda purchase: purchase.date, reverse = reverse)
        print("Sorting ledger by date")
        self.print_ledger()

    # --------------------------------------------------------------------------------

    # sorting list by price
    def sorting_by_price(self, reverse = False):
        self.purchases_list = sorted(self.purchases_list, key=lambda purchase: purchase.price, reverse = reverse)
        print("Sorting ledger by price")
        self.print_ledger()

    # ------------------------------------------------------------------------------------------------------------------------------

    def sorting_total_sales_by_store(self):
        # print header
        print("{:<12}                  {:<13}".format("Store", "Sum of sales"))

        # init dictionary
        sum_sales_by_store_dict = {}
        for store in self.stores_list:
            sum_sales_by_store_dict[store] = 0

        # compute dictionary
        for purchase in self.purchases_list:
            sum_sales_by_store_dict[purchase.store] += purchase.price

        # sort dictionary
        list_of_tuples = sorted(sum_sales_by_store_dict.items(), key=lambda x: x[1], reverse=True)

        # print dictionary
        for elem in list_of_tuples:
            print("{:<22}        {:<25}".format(elem[0], round(elem[1], 2)))

        print("-" * 100)

    # ------------------------------------------------------------------------------------------------------------------------------
    def sorting_total_sales_by_category(self):
        # print header
        print("{:<12}                  {:<13}".format("Category", "Sum of sales"))

        # init dictionary
        sum_sales_by_category_dict = {}
        for category in self.categories_list:
            sum_sales_by_category_dict[category] = 0

        # compute dictionary
        for purchase in self.purchases_list:
            sum_sales_by_category_dict[purchase.category] += purchase.price

        # sort dictionary
        list_of_tuples = sorted(sum_sales_by_category_dict.items(), key=lambda x: x[1], reverse=True)

        # print dictionary
        for elem in list_of_tuples:
            print("{:<22}        {:<25}".format(elem[0], round(elem[1], 2)))

        print("-" * 100)
    # ------------------------------------------------------------------------------------------------------------------------------
    def statistics_by_store(self, enter_store):
        list_of_prices = [purchase.price for purchase in self.purchases_list if purchase.store == enter_store]

        min_price = min(list_of_prices)
        max_price = max(list_of_prices)
        count_price = len(list_of_prices)
        sum_price = sum(list_of_prices)
        avg_price = sum_price / float(count_price)

        round_sum_price = round(sum_price, 2)
        round_avg_price = round(avg_price, 2)

        print(
            "{:<15}        {:<15}  {:<15}{:<15}     {:<15}   {:<15}".format("Store", "Min Price", "Max Price", "Count",
                                                                            "Sum", "Average"))
        print("{:<15}        {:<15}  {:<15}{:<15}     {:<15}   {:<15}".format(enter_store, min_price, max_price,
                                                                              count_price,
                                                                              round_sum_price, round_avg_price))
        print("-" * 100)

    # ------------------------------------------------------------------------------------------------------------------------------
    def statistics_by_category(self, enter_category):
        list_of_prices = [purchase.price for purchase in self.purchases_list if purchase.category == enter_category]

        min_price = min(list_of_prices)
        max_price = max(list_of_prices)
        count_price = len(list_of_prices)
        sum_price = sum(list_of_prices)
        avg_price = sum_price / float(count_price)

        round_sum_price = round(sum_price, 2)
        round_avg_price = round(avg_price, 2)

        print("{:<15}        {:<15}  {:<15}{:<15}     {:<15}   {:<15}".format("Category", "Min Price", "Max Price",
                                                                              "Count",
                                                                              "Sum", "Average"))
        print("{:<15}        {:<15}  {:<15}{:<15}     {:<15}   {:<15}".format(enter_category, min_price, max_price,
                                                                              count_price,
                                                                              round_sum_price, round_avg_price))
        print("-" * 100)

    # ------------------------------------------------------------------------------------------------------------------------------
    # filter_stores
    def filter_stores(self, pattern):
        filter_list = [purchase for purchase in self.purchases_list if re.search(pattern, purchase.store)]
        print("Found", len(filter_list), "results.")

        print("{:<10}        {:<9}  {:<15}   {:<25}  {:<15}  {:<20}".format("Date"
                                                                            , "Time", "Store", "Category", "Price",
                                                                            "Payment"))

        for purchase in filter_list:
            print("{}        {}      {:<15}   {:<25}  {:<15}  {:<20}".format(purchase.date
                                                                             , purchase.time, purchase.store,
                                                                             purchase.category, purchase.price,
                                                                             purchase.payment))

        print("-" * 100)


########################################
# Create empty Ledger object
########################################

ledger = Ledger()

#########################################
# read purchases file
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
        curr_purchase = Purchase(date, time, store, category, float(price), payment)

        # add to store list
        if store not in ledger.get_all_stores():
            ledger.add_store(store)

        # add to category list
        if category not in ledger.get_all_categories():
            ledger.add_category(category)

        # add purchase to ledger
        ledger.add_purchase(curr_purchase)


#########################################
# Main Menu helper functions
#########################################

def print_welcome_msg():
    print("Welcome to the U.S. Ledger of online purchases!")


def print_menu():
    print()
    print("~" * 30)
    print("** 1.  Print all stores. **")
    print("** 2.  Print all categories. **")
    print("** 3.  Count purchases. **")
    print("** 4.  Sort ledger by date ascending. **")
    print("** 5.  Sort ledger by date descending. **")
    print("** 6.  Sort ledger by price ascending. **")
    print("** 7.  Sort ledger by price descending. **")
    print("** 8.  Statistical summary for selected store. **")
    print("** 9.  Statistical summary for selected category. **")
    print("** 10. Sum of sales by stores. **")
    print("** 11. Sum of sales by categories. **")
    print("** 12. Filter Ledger by store pattern. **")
    print('** 13. Quit. **')
    print("~" * 30)
    print()


def get_user_input():
    print_menu()
    str_choice = input("Please enter your choice: ")
    try:
        choice = int(str_choice)
    except:
        return -1
    return choice

#########################################
# Main Menu loop
#########################################

print_welcome_msg()

while True:
    choice = get_user_input()
    if (choice == 1):
        ledger.print_stores()
    elif (choice == 2):
        ledger.print_categories()
    elif (choice == 3):
        print("Count of purchases:", ledger.count_purchases())
    elif (choice == 4):
        ledger.sorting_by_date()
    elif (choice == 5):
        ledger.sorting_by_date(True)
    elif (choice == 6):
        ledger.sorting_by_price()
    elif (choice == 7):
        ledger.sorting_by_price(True)
    elif (choice == 8):
        store = input("Please enter store: ")
        if store not in ledger.get_all_stores():
            print("No such store in data.")
        else:
            ledger.statistics_by_store(store)
    elif (choice == 9):
        category = input("Please enter category: ")
        if category not in ledger.get_all_categories():
            print("No such category in data.")
        else:
            ledger.statistics_by_category(category)
    elif (choice == 10):
        ledger.sorting_total_sales_by_store()
    elif (choice == 11):
        ledger.sorting_total_sales_by_category()
    elif (choice == 12):
        pattern = input("Please enter store pattern: ")
        ledger.filter_stores(pattern);
    elif (choice == 13):
        print("Quitting...")
        break
    else:
        print("Illegal choice.")
