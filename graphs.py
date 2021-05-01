#############################################
# Filename: graphs.py
# Author: Roni Shternberg
# Generate graphs using pandas and matplotlib
#############################################

#########################################
# Import Statements
#########################################

import pandas as pd
import matplotlib.pyplot as plt

########################################################
# Writing new file header. We only need to do this ONCE. 
########################################################

#orig_df = pd.read_csv("purchases1000_new.txt", delimiter='\t', header=None)

#header = ["Date", "Time", "Store", "Category", "Price", "Payment"]

#orig_df.to_csv("purchases1000_new_with_header.txt", header=header, index=False)

####################################################
# Once this file is ready, read from it using pandas
####################################################

df = pd.read_csv("purchases1000_new_with_header.txt",
    header=0, index_col=0, parse_dates=True, squeeze=True)
# DEBUG
#print(df)
#print("-" * 90)

#######################################
# plot_pie function: 
# input: pie type - Payment or Category
# will be called from runGui
#######################################

def plot_pie(pie_type): 
    val_counts = df[pie_type].value_counts() 
    print("value counts")
    print(val_counts)
    print("-" * 30)
    
    plt.pie(val_counts, labels = val_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title(pie_type + " distribution", 
              fontdict={'fontsize': 14, 'fontweight':'bold'})
    plt.show()

def plot_scatter():
    #df.plot()
    df.groupby("Date").sum().plot() # (default is kind="line")
    
    plt.title("Sales over time", 
              fontdict={'fontsize': 14, 'fontweight':'bold'})
    plt.show()

# DEBUG:
#plot_pie("Payment")
#plot_pie("Category")
#plot_scatter()