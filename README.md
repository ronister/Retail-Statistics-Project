# purchases
This project takes purchases data csv file (ledger of sales) and runs various statistics on it using:
(a) textual interface (run.py), or:
(b) Tkinter standard python GUI library (runGui.py).
Each Purchase has 6 fields: date, time, store, category, price, and payment method (Visa, Cash, etc.)
Notes:
1. The dataset was taken from Udacity's Massive Open Online Course (MOOC) "Intro to Hadoop and MapReduce" (https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617)
2. The original "purchases.txt" data file was huge (about 200 MB). Plus the dates were from the year 2012 only. (1/1/2012 to 31/12/2012)
3. Because the file was huge, we decided to take the first 1000 purchases (using UNIX shell command "head"). The result was about 50 KB - we called it "purchases1000.txt" file.
4. The problem now was that the dates in "purchases1000.txt" file were all from the same day - 2012-01-01.
5. In order to have different dates and times, we use the script prepare.py. This script creates lists of random dates and times, and sets them into the purchase objects using the Purchase method set_date_and_time(). We called the result "purchases1000_new.txt" file.

Other files:

purchase_and_ledger.py - Purchase and Ledger Class definitions

graphs.py - Used to Generate graphs using pandas and matplotlib

This project features:
- OOP Classes
- textual interface using input() function and exception handling 
- tkinter GUI module
- csv, datetime, random, collections and re modules
- statistics module
- List Comprehensions, dictionaries, sorting with lambdas, etc
- a bit of pandas and matplotlib to generate 2 pie plots
