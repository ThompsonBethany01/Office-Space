import pandas as pd
import numpy as np

def create_data(transactions):
    '''
    Creates a df of fake bank transactions - set the amount of transactions with this parameter.
    Includes the account total, interest rate, earned interest, and total after interest.
    Generates different random values each time function is run.
    '''
   # random floats generated with average of 8,000 and stddev of 1,500
    totals = np.random.normal(8_000, 1_500, transactions + 1)
    
    # random floats generated from [0, 1.0)
    # multiply by .1 to mimick average interest rates, typically .06
    interest = np.random.random(transactions + 1) * .1
    
    # creating an empty df with an index starting at 1 and ending at 100,000,000
    df = pd.DataFrame(index=range(1,transactions + 1))
    
    # creating a column in the df as the account balance using random array created earlier
    df['balance'] = pd.DataFrame(totals)
    
    # creating a column in the df as the interest rate using random array created earlier
    df['interest_rate'] = pd.DataFrame(interest)
    
    # creating a new column by calculating the interest with our existing columns
    # the amount of interest earned is the account balance times the interest rate
    df['calculated_interest'] = df.balance * df.interest_rate
    
    # creating a new column by calculating the total with our existing columns
    # the new total is the account balance plus the interest earned
    df['new_balance'] = df.balance + df.calculated_interest
    
    return df