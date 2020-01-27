def non_prime(n):
    if not n % 2:
        return n - 1
    
    for number in range(3, int((n * 0.5) + 1), 2):
        if not n % number:
            return n - 1

    return False

def manipulate_generator(generator, n):
    """
    This function must manipulate the generator functions
    so that the first k non-prime positive integers are
    printed, each on a separate line.
    """
    while True:
        n += 1
        if n < 3:
            continue
        
        num = non_prime(n)
        if num:
            return generator.send(num) 


""" The following code cannot be modified except for debugging """

def positive_integers_generator():
    n = 1
    while True:
        x = yield n
        if x is not None:
            n = x
        else:
            n += 1

if __name__ == '__main__':
    """
    Given an integer k, print the first k non-prime positive integers,
    each on a new line. For example, if k = 10, the output would be:

    1 4 6 8 9 10 12 14 15 16
    """
    k = int(input())
    g = positive_integers_generator()
    for _ in range(k):
        n = next(g)
        print(n)
        manipulate_generator(g, n)

        """
        Test 1:
        - Inputs
            12

        - Outpus
            1 4 6 8 9 10 12 14 15 16 18 20
        """