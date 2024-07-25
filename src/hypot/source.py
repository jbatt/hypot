# Requirements

# 2 inputs, integer or float (is digit), positive
# 1 output, float, positive
# external library? No external library
# create a function to calculate the hypot = sqrt(a^2 + b^2)
# create a squ are root function: positive number, returns float

# create a square root function: positive number, returns float
def sqrt(a):
    """Calculates the square root of an input number. 
    If the input is negative, the absolute value of the input is taken. 

    Args:
        a (int,float): input number (positive or negative)

    Returns:
        float: square root of the input
    """
    return abs(a)**0.5

# create a function to calculate the hypot = sqrt(a^2 + b^2)
def hypot(opp, adj):
    """Calculates the legnth of the hypotenuse of a 
    right-angled triangle using Pythagorus' theorum
    hypot = sqrt(opp^2 + adj^2)

    Args:
        opp (int, float): length of opposite side of triangle
        adj (int, float): length of adjacent side of triangle

    Returns:
        float: length of hypotenuse
    """
    hyp_sq = opp**2 + adj**2
    hyp = sqrt(hyp_sq)    
    
    return hyp

