#########################################
# Filename: purchase_and_ledger_not_working.py
# Author: Roni Shternberg
# Purchase and Ledger Class definitions
#########################################

#########################################
# Import Statements
#########################################

import re  # regular expressions
from statistics import mean, stdev
from collections import defaultdict

#########################################
# Constants
#########################################

TYPE_STORE = "Store"
TYPE_CATEGORY = "Category"
TYPE_PAYMENT = "Payment"

LINE_WIDTH = 107

#########################################
# Purchase class
#########################################

class Purchase:

    def __init__(self, date, time, store, category, price, payment):
        self.date = date
        self.time = time
        self.store = store
        self.category = category
        self.price = price
        self.payment = payment

#########################################
# Ledger class
# Ledger = account book, record book - "a book or other collection of financial accounts of a particular type."
#########################################

class Ledger:  

    def __init__(self):
        self.purchases_list = []  # list of purchase_and_ledger_not_working objects
        self.stores_list = []  # list of names of different stores
        self.categories_list = []  # list of names of unique categories
        self.payments_list = [] # list of payment methods

    # get list of stores
    def get_all_stores(self):
        return self.stores_list

    # get list of categories
    def get_all_categories(self):
        return self.categories_list

    # get list of payment methods
    def get_all_payments(self):
        return self.payments_list

    # ------------------------

    # add to list of purchases
    def add_purchase(self, purchase):
        self.purchases_list.append(purchase)

    # add to list of stores
    def add_store(self, store):
        self.stores_list.append(store)

    # add to list of categories
    def add_category(self, category):
        self.categories_list.append(category)

    # add to list of payment methods
    def add_payment(self, payment):
        self.payments_list.append(payment)

    # ------------------------
    # count number of purchases
    def count_purchases(self):
        return len(self.purchases_list)

    # get purchase_and_ledger_not_working at index i
    def get_purchase_at(self, i):
        return self.purchases_list[i]

    # ---------------------------------------------------------------------------
    # print list of stores
    def print_stores(self):
        self.stores_list = sorted(self.stores_list)
        for store in self.stores_list:
            print(store)
        print("Total of", len(self.stores_list), "stores.")
        print("-" * LINE_WIDTH)

    # ---------------------------------------------------------------------------
    # print list of categories
    def print_categories(self):
        self.categories_list = sorted(self.categories_list)
        for category in self.categories_list:
            print(category)
        print("Total of", len(self.categories_list), "categories.")
        print("-" * LINE_WIDTH)
    # ---------------------------------------------------------------------------
    # print list of payment methods
    def print_payments(self):
        self.payments_list = sorted(self.payments_list)
        for payment in self.payments_list:
            print(payment)
        print("Total of", len(self.payments_list), "payment methods.")
        print("-" * LINE_WIDTH)

    # --------------------------------------------------------------------------------
    # sorting list by date
    def sorting_by_date(self, reverse = False):
        self.purchases_list = sorted(self.purchases_list, key=lambda purchase: purchase.date, reverse = reverse)
        print("Sorting ledger by date")
        self.print_ledger(self.purchases_list)

    # --------------------------------------------------------------------------------
    # sorting list by price
    def sorting_by_price(self, reverse = False):
        self.purchases_list = sorted(self.purchases_list, key=lambda purchase: purchase.price, reverse = reverse)
        print("Sorting ledger by price")
        self.print_ledger(self.purchases_list)

    # ------------------------------------------------------------------------------------------------------------------------------
    
    def statistics_by_store(self, entered_store):
        list_of_purchases_of_store = [purchase for purchase in self.purchases_list if purchase.store == entered_store]
        
        list_of_prices = [purchase.price for purchase in list_of_purchases_of_store]
        
        total_for_store = sum(list_of_prices)
        
        self.statistics_by(list_of_prices, TYPE_STORE, entered_store)
        
        # init dictionaries
        sales_dict = defaultdict(list)
        sum_sales_dict = defaultdict(list)
        count_sales_dict = defaultdict(list)
        mean_sales_dict = defaultdict(list)
        pct_sales_dict = defaultdict(list)

        # compute dictionary for only purchases with entered_store
        for purchase in list_of_purchases_of_store:
            sales_dict[purchase.category].append(purchase.price)
                         
        # We go over the categories in the sales dictionary, NOT over the self.categories_list. This is because categories that
        # aren't in the dictionary have empty list of prices. This means that sum() will be 0, and mean() will
        # return: "StatisticsError: mean requires at least one data point"
        for category in sales_dict:
            sum_sales_dict[category] = sum(sales_dict[category])
            count_sales_dict[category] = len(sales_dict[category])
            mean_sales_dict[category] = mean(sales_dict[category])
            pct_sales_dict[category] = sum_sales_dict[category] / total_for_store * 100

        # sort sum sales dictionary
        list_of_tuples = sorted(pct_sales_dict.items(), key=lambda x: x[1], reverse=True)

        # print header
        print("{:<12}                   {:<13}        {:<12}      {:<15}       {:<25}    {:<15}".format(
            TYPE_CATEGORY, "Sum for Store", "Count", "Mean for Store", "Total Sales for Store", "Sum / Total (%)"))
 
        # print category, sum, count, mean, total, percentage.
        for category, val_pct in list_of_tuples:
            val_sum = sum_sales_dict[category]
            val_count = count_sales_dict[category]
            val_mean = mean_sales_dict[category]

            print("{:<17}              {:<13}        {:<12}      {:<15}       {:<25}    {:<15}".format(
                category, round(val_sum, 2), val_count, round(val_mean, 2), round(total_for_store, 2), round(val_pct)))

        print("-" * LINE_WIDTH)
        
    # ------------------------------------------------------------------------------------------------------------------------------
        
    def statistics_by_category(self, entered_category):
        list_of_purchases_of_category = [purchase for purchase in self.purchases_list if purchase.category == entered_category]
        
        list_of_prices = [purchase.price for purchase in list_of_purchases_of_category]

        self.statistics_by(list_of_prices, TYPE_CATEGORY, entered_category)
        
        # init dictionaries
        sales_dict = defaultdict(list)
        sum_sales_dict = defaultdict(list)
        count_sales_dict = defaultdict(list)
        mean_sales_dict = defaultdict(list)
        total_sales_dict = defaultdict(list)
        pct_sales_dict = defaultdict(list)

        # compute dictionary for only purchases with entered_category
        for purchase in list_of_purchases_of_category:
            sales_dict[purchase.store].append(purchase.price)

        # compute dictionary for all purchases
        for purchase in self.purchases_list:
            total_sales_dict[purchase.store].append(purchase.price)

        for store in self.stores_list:
            total_sales_dict[store] = sum(total_sales_dict[store])

        # We go over the stores in the sales dictionary, NOT over the self.stores_list. This is because stores that
        # aren't in the dictionary have empty list of prices. This means that sum() will be 0, and mean() will
        # return: "StatisticsError: mean requires at least one data point"
        for store in sales_dict:
            sum_sales_dict[store] = sum(sales_dict[store])
            count_sales_dict[store] = len(sales_dict[store])
            mean_sales_dict[store] = mean(sales_dict[store])
            pct_sales_dict[store] = sum_sales_dict[store] / total_sales_dict[store] * 100

        # sort sum sales dictionary
        list_of_tuples = sorted(pct_sales_dict.items(), key=lambda x: x[1], reverse=True)

        # print header
        print("{:<12}               {:<13}      {:<12}      {:<15}      {:<25}    {:<15}".format(
            TYPE_STORE, "Sum for Category", "Count", "Mean for Category", "Total Sales for Store", "Sum / Total (%)"))
  
        # print store, sum, count, mean, total, percentage.
        for store, val_pct in list_of_tuples:
            val_sum = sum_sales_dict[store]
            val_count = count_sales_dict[store]
            val_mean = mean_sales_dict[store]
            val_total = total_sales_dict[store]

            print("{:<16}           {:<13}         {:<12}      {:<15}        {:<25}    {:<15}".format(
                store, round(val_sum, 2), val_count, round(val_mean, 2), round(val_total, 2), round(val_pct)))

        print("-" * LINE_WIDTH)
                
    # ------------------------------------------------------------------------------------------------------------------------------
    def statistics_by_payment(self, entered_payment):
        list_of_purchases_of_payment = [purchase for purchase in self.purchases_list if purchase.payment == entered_payment]
        
        list_of_prices = [purchase.price for purchase in list_of_purchases_of_payment]
        
        self.statistics_by(list_of_prices, TYPE_PAYMENT, entered_payment)

        # init dictionaries
        sales_dict = defaultdict(list)
        sum_sales_dict = defaultdict(list)
        count_sales_dict = defaultdict(list)
        mean_sales_dict = defaultdict(list)
        total_sales_dict = defaultdict(list)
        pct_sales_dict = defaultdict(list)

        # compute dictionary for only purchases with entered_payment
        for purchase in list_of_purchases_of_payment:
            sales_dict[purchase.store].append(purchase.price)

        # compute dictionary for all purchases
        for purchase in self.purchases_list:
            total_sales_dict[purchase.store].append(purchase.price)

        for store in self.stores_list:
            total_sales_dict[store] = sum(total_sales_dict[store])

        # We go over the stores in the sales dictionary, NOT over the self.stores_list. This is because stores that
        # aren't in the dictionary have empty list of prices. This means that sum() will be 0, and mean() will
        # return: "StatisticsError: mean requires at least one data point"
        for store in sales_dict:
            sum_sales_dict[store] = sum(sales_dict[store])
            count_sales_dict[store] = len(sales_dict[store])
            mean_sales_dict[store] = mean(sales_dict[store])
            pct_sales_dict[store] = sum_sales_dict[store] / total_sales_dict[store] * 100

        # sort percentage sales dictionary
        list_of_tuples = sorted(pct_sales_dict.items(), key=lambda x: x[1], reverse=True)

        # print header
        print("{:<12}               {:<13}      {:<12}      {:<15}      {:<25}    {:<15}".format(
            TYPE_STORE, "Sum for Payment", "Count", "Mean for Payment", "Total Sales for Store", "Sum / Total (%)"))

        # # print header - Avital
        # print("{:<12}               {:<13}      {:<12}      {:<15}      {:<25}    {:<15}".format(
        #     TYPE_STORE, "Sum by Payment method", "# of Sales", "Mean for Payment", "Total Sales for Store", "Payment method percentage"))

        # print store, sum, mean, total, percentage.
        for store, val_pct in list_of_tuples:
            val_sum = sum_sales_dict[store]
            val_count = count_sales_dict[store]
            val_mean = mean_sales_dict[store]
            val_total = total_sales_dict[store]

            print("{:<16}           {:<13}        {:<12}      {:<15}       {:<25}    {:<15}".format(
                store, round(val_sum, 2), val_count, round(val_mean, 2), round(val_total, 2), round(val_pct)))

        print("-" * LINE_WIDTH)
        

    # ------------------------------------------------------------------------------------------------------------------------------
    def sorting_total_sales_by_store(self):
        # init dictionary
        sales_dict = defaultdict(int)

        # compute dictionary
        for purchase in self.purchases_list:
            sales_dict[purchase.store] += purchase.price

        self.sorting_total_sales_by(sales_dict, TYPE_STORE, "Sum of Sales")

    # ------------------------------------------------------------------------------------------------------------------------------
    def sorting_total_sales_by_category(self):
        # init dictionary
        sales_dict = defaultdict(int)

        # compute dictionary
        for purchase in self.purchases_list:
            sales_dict[purchase.category] += purchase.price

        self.sorting_total_sales_by(sales_dict, TYPE_CATEGORY, "Sum of Sales")

    # ------------------------------------------------------------------------------------------------------------------------------
    def sorting_total_sales_by_payment(self):
        # init dictionary
        sales_dict = defaultdict(int)

        # compute dictionary
        for purchase in self.purchases_list:
            sales_dict[purchase.payment] += purchase.price

        self.sorting_total_sales_by(sales_dict, TYPE_PAYMENT, "Sum of Sales")

    # ------------------------------------------------------------------------------------------------------------------------------

    def sorting_std_sales_by_store(self):
        # init dictionaries
        sales_dict = defaultdict(list)
        std_sales_dict = defaultdict(list)
        mean_sales_dict = defaultdict(list)
        
        # compute sales dictionary
        for purchase in self.purchases_list:
            sales_dict[purchase.store].append(purchase.price)
                
        for store in self.stores_list:
            std_sales_dict[store] = stdev(sales_dict[store])
            mean_sales_dict[store] = mean(sales_dict[store])
        
        # sort std sales dictionary
        list_of_tuples = sorted(std_sales_dict.items(), key=lambda x: x[1], reverse=True)
        
        # print header
        print("{:<12}                      {:<13}    {:<15}".format(TYPE_STORE, "Std", "Mean"))
        
        # print store, std, mean
        for store, val_std in list_of_tuples:
            val_mean = mean_sales_dict[store]
            print("{:<16}                  {:<13}    {:<15}".format(store, round(val_std, 2), round(val_mean, 2)))
        print("-" * LINE_WIDTH)
        
    # ------------------------------------------------------------------------------------------------------------------------------
    # filter ledger by store pattern
    def filter_stores(self, pattern):
        filtered_list = [purchase for purchase in self.purchases_list if re.search(pattern.lower(), purchase.store.lower())]
        print("Found", len(filtered_list), "results.")

        self.print_ledger(filtered_list)

    ####################################
    # Helper methods
    ####################################

    # print list of purchases in ledger
    def print_ledger(self, purchases_list):
        # print header
        print("{:<10}        {:<9}  {:<15}   {:<25}  {:<15}  {:<20}".format("Date", "Time",
                                                                            "Store", "Category",
                                                                            "Price", "Payment"))
        # print data
        for purchase in purchases_list:
            print("{}        {}      {:<15}   {:<25}  {:<15}  {:<20}".format(purchase.date, purchase.time,
                                                                             purchase.store, purchase.category,
                                                                             purchase.price, purchase.payment))
        print("-" * LINE_WIDTH)

    # ------------------------------------------------------------------------------------------------------------------------------
    def sorting_total_sales_by(self, sales_dict, query_type, text):
        # sort dictionary
        list_of_tuples = sorted(sales_dict.items(), key=lambda x: x[1], reverse=True)

        # print header
        print("{:<12}                  {:<13}".format(query_type, text))
        # print dictionary
        for elem in list_of_tuples:
            print("{:<22}        {:<25}".format(elem[0], round(elem[1], 2)))
        print("-" * LINE_WIDTH)

    # ------------------------------------------------------------------------------------------------------------------------------
    def statistics_by(self, list_of_prices, query_type, entered_value):

        min_price = min(list_of_prices)
        max_price = max(list_of_prices)
        count_price = len(list_of_prices)
        sum_price = sum(list_of_prices)
        mean_price = mean(list_of_prices) # can also be computed as: mean_price = sum_price / float(count_price)
        std_price = stdev(list_of_prices)

        round_sum_price = round(sum_price, 2)
        round_mean_price = round(mean_price, 2)
        round_std_price = round(std_price, 2)

        # print header
        print("{:<15}   {:<15}  {:<15}{:<15}{:<15}   {:<15}   {:<15}".format(query_type, "Min Price", "Max Price",
                                                                                "Count", "Sum", "Mean", "Std"))
        # print stats
        print("{:<15}   {:<15}  {:<15}{:<15}{:<15}   {:<15}   {:<15}".format(entered_value, min_price, max_price,
                                                                                count_price, round_sum_price,
                                                                                round_mean_price, round_std_price))
        print("-" * LINE_WIDTH)

