# Multiply two arbitrarily large numbers x and y stored as strings
def multiply(x, y):
    # Strip zeroes for x and y to reduce unnecessary computations
    x = stripLeadingZeroes(x)
    y = stripLeadingZeroes(y)

    # Initialize product string z
    z = ""

    # Iterate through x backwards, multiply each digit by y, and add the product to z
    for i in range(len(x)-1, -1, -1):
        subprod = multiplySingleDig(y, x[i]) + ("0" * (len(x) - i - 1))
        z = add(z, subprod)

    return(z)

# Remove unneccesary zeroes from the beginning of a number x
def stripLeadingZeroes(x):
    # Iterate through x and return the rest of x when a non-zero character is encountered
    for i in range(len(x)):
        if x[i] != "0":
            return(x[i:])
    return("0") # Return "0" if number does not have any non-zero characters

# Multiply an arbitrarily large number x by a single digit number y
def multiplySingleDig(x, y):
    
    # Initialize product and carry
    z = ""
    carry = 0
    
    # Iterate backwards through x
    for i in range(len(x)-1, -1, -1):

        # Evaluate product of single digit in x and y
        rawprod = int(x[i]) * int(y) + carry

        # Find units digit and tens digit of the raw product
        finalprod = rawprod % 10
        carry = rawprod // 10

        # Add the units digit to the beginning of z
        z = str(finalprod) + z
    # If the carry digit is not 0, then add it to the beginning of z
    if carry != 0:
        z = str(carry) + z
    return(z)

# Add two arbitrarily large numbers x and y stored as strings
def add(x, y):
    # Make sure that x is always longer than y or the same length as y
    if (len(x) < len(y)):
        x,y = y,x

    # Initialize sum and carry
    z = ""
    carry = 0

    # Iterate through x backwards using negative indices
    for i in range(-1, -len(x)-1, -1):
        try:
            rawsum = int(x[i]) + int(y[i]) + carry
        
        # If y is shorter than x, then it will not always have a digit at index i, so this prevents a IndexError being thrown
        except IndexError:
            rawsum = int(x[i]) + carry
        
        # Find units digit and tens digit of the raw sum
        finalsum = rawsum % 10
        carry = rawsum // 10

        # Add the units digit to the beginning of z
        z = str(finalsum) + z
    # If the carry digit is not 0, then add it to the beginning of z
    if carry != 0:
        z = str(carry) + z
    return(z)