import pandas as import pd
import numpy as np

def create_data():
    '''
    Creates a df of fake bank transactions.
    Includes the account total, interest rate, earned interest, and total after interest.
    Generates different random values each time function is run.
    '''
    # set the number of observations for random values as 100,000 transactions
    observations = 100_000
    
    # random floats generated with average of 8,000 and stddev of 1,500
    totals = np.random.normal(8_000, 1_500, observations)
    
    # random floats generated from [0, 1.0)
    # multiply by .1 to mimick average interest rates, typically .06
    interest = np.random.random(observations) * .1
    
    # creating an empty df with an index starting at. and ending at 1,000
    df = pd.DataFrame(index=range(1,1001))
    
    # creating a column in the df as the account balance using random array created earlier
    df['balances'] = pd.DataFrame(totals)
    
    # creating a column in the df as the interest rate using random array created earlier
    df['interest_rate'] = pd.DataFrame(interest)
    
    # creating a new column by calculating the interest with our existing columns
    # the amount of interest earned is the account balance times the interest rate
    df['calculated_interest'] = df.balances * df.interest_rate
    
    # creating a new column by calculating the total with our existing columns
    # the new total is the account balance plus the interest earned
    df['new_balance'] = df.balances + df.calculated_interest
    
    return df