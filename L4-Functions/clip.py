def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    # Your code here
    return min(max(lo,x),hi)
