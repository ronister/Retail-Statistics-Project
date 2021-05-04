# purchases
This project takes purchases data file (ledger of sales) and runs some statistics on it using:
(a) textual interface (run.py), or:
(b) Tkinter standard python GUI library (runGui.py).
Each Purchase has 6 fields: date, time, store, category, price, and payment method (Visa, Cash, etc.)
Notes:
1. The Original "purchases.txt" data file was about 200 MB, and the dates are from the year 2012. (1/1/2012 to 31/12/2012)
2. 200MB is too big, so we took the first 1000 purchases (UNIX shell command "head") --- the result was about 50 KB.
3. We prepare the "purchases1000_new.txt" file in a script called "prepare.py" (see below)

purchase_and_ledger.py - Purchase and Ledger Class definitions

graphs.py - Used to Generate graphs using pandas and matplotlib

prepare.py - 
This script prepares the "purchases1000_new.txt" data file based on "purchases1000.txt" file.
1. All the dates in "purchases1000.txt" file are from the same day - 2012-01-01.
2. In order to have different dates, we create lists of RANDOM dates and times.
3. We set dates and times into the purchase objects using the Purchase method set_date_and_time().
