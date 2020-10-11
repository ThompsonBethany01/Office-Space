# import modules to create data and take the pennies from the 7-11 tray
import Data
import Floppy_Disk

# import python modules
import pandas as pd
import numpy as np

# import date function for bank statement
from datetime import date

def print_statement(deposit):
    '''
    Prints the statemnt for the balance of our account.
    Hopefully an amount not noticable to corporate.
    '''
    print('____________________________________________________________\n')
    print(date.today(),'XXXXXXXXXXXXXX5976\n')
    print('BALANCE INQUIRY FROM SAVINGS')
    print(round(deposit,2))
    print('____________________________________________________________')

def deposits(transactions):
    '''
    Calculates the amount deposited over the course of a week, 5 days.
    transactions parameter is how many transactions to be completed for each day.
    '''

    # days to calculate deposits, 5 days
    days = range(1,5)

    # sets initial amount to 0
    deposit = 0
    
    # loops through deposits for each days
    for x in days:
        # creates different data for each day
        df = Data.create_data(transactions)

        # calculates the deposit of taking the leftover rounded amounts
        deposit += Floppy_Disk.virus_cdef(df)
        
    # returns the bank statement of how much balance in account
    return print_statement(deposit)