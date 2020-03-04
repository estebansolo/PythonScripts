from collections import defaultdict

# Here we initialize the dict where will be the numbers with the factors
factors = defaultdict(list)

# This runs over every number from 1 to 100
for number in range(1, 101):
    """
    A for loop that runs over every number(y) from 1 to the half plus one,
    this because a number(x) cannot be divisible by any number(y) from the
    second half besides the number(x) that's why at the end we add the same
    number to the factors
    
    double // divide integers for example 5 // 2 = 2 (not 2.5)
    """
    for factor in range(1, int(number // 2) + 1):
        # Check if the first number is factor (x % y == 0)
        if number % factor == 0:
            # If it's factor of the number we added to factors list
            factors[number].append(factor)
    
    # We add the same number becuase you can divide the same number by itself 
    # 50 in 50 (50 % 50 == 0)
    # 23 / 23 = 0 ... 81 / 81 = 0 ... etc ...
    factors[number].append(number)
    
print(factors)