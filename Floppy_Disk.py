def virus_cdef(df):
    '''
    This function rounds down all interest calculations and returns the total
    of what is leftover from all these rounded amounts.
    A bug is making it deposit a larger amount than anticipated.
    '''
    for transaction in df.index:
    
        # variable holds the rounded balance of the account
        rounded = round(df.new_balance[transaction], 1)
    
        # variable holds the original balance before rounding
        original = df.new_balance[transaction]
    
        # this is what would be deposited into our account, does not account for rounding up or down
        deposit = rounded - original
    
        # sets the initial balance of our account at 0
        total = 0
    
        # conditional checks if the balance is rounded up or down
        # if the deposit is negative, the balance was rounded down
        if deposit < 0:
        
            # add the absolute value of the deposited, since the calculation makes it negative
            total += abs(deposit)
        
        # if the deposit is positive, it was rounded up
        elif deposit > 0:
            # to make it rounded down, we subtract a penny from the total of the rounded amount
            rounded = rounded - 1
        
            # now we can recalculate the deposit amount
            deposit = rounded - original
        
            # add the absolute value of the deposited, since the calculation makes it negative
            total += abs(deposit)
        
    return total