#########################################
# Filename: prepare.py
# Author: Roni Shternberg
# This script prepares the "purchases1000_new.txt" data file based on "purchases1000.txt" file.
# 1. All the dates in "purchases1000.txt" file are from the date "2012-01-01".
# 2. In order to have different dates, we create lists of RANDOM dates and times.
# 3. We set dates and times into the purchase objects using the Purchase method set_date_and_time().
#########################################

#########################################
# Import Statements
#########################################

from datetime import datetime
import random
import csv  # comma seperated values

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

    # we use this method to set random date and time into purchase objects.
    def set_date_and_time(self, date_obj, time_str):
        self.date = date_obj
        self.time = time_str

class Ledger:  # account book, record book - "a book or other collection of financial accounts of a particular type."

    def __init__(self):
        self.purchases_list = []  # list of purchase objects

   # add to list of purchases
    def add_purchase(self, purchase):
        self.purchases_list.append(purchase)

    # get purchase at index i
    def get_purchase_at(self, i):
        return self.purchases_list[i]

############################################
# Generate random dates and times, and hold them in temp lists.
# values from these temp lists will be set into purchase objects using the set_date_and_time() method, later on.
############################################

list_date_objects = []
list_time_strings = []

for i in range(1, 1001):
    # randomize yyyy-mm-dd values
    curr_year = random.randint(2000, 2020)
    curr_month = random.randint(1, 12)
    curr_day = random.randint(1, 28)

    # cast int values into strings
    date_str = str(curr_year) + '-' + str(curr_month) + '-' + str(curr_day)

    # format the date string
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()

    # append date object into temp list
    list_date_objects.append(date_obj)

    # same for time values
    curr_hour = random.randint(0, 23)
    curr_min = random.randint(0, 59)

    # cast int values to strings
    time_str = str(curr_hour) + ':' + str(curr_min)
    time_obj = datetime.strptime(time_str, '%H:%M').time()
    time_str = str(time_obj)[:5]

    # unlike dates, we append the time string into the temp list, not the time object,
    # since we don't really do anything with times.
    list_time_strings.append(time_str)

########################################
# Create empty Ledger object
########################################

ledger = Ledger()

#########################################
# read "purchases1000.txt" file
#########################################

with open("purchases1000.txt") as csv_file:
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

        # add purchase to ledger
        ledger.add_purchase(curr_purchase)

##################################################################################
# setting the random dates and times from the temp lists into purchase objects
##################################################################################

for i in range(1000):
    ledger.get_purchase_at(i).set_date_and_time(list_date_objects[i], list_time_strings[i])


##################################################################################
# Writing the "purchases1000_new.txt" file
##################################################################################

with open("purchases1000_new.txt", mode='w', newline='') as csv_new_file:
    csv_writer = csv.writer(csv_new_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in range(1000):
        purchase = ledger.get_purchase_at(i)
        csv_writer.writerow(
            [purchase.date, purchase.time, purchase.store, purchase.category, purchase.price, purchase.payment])
