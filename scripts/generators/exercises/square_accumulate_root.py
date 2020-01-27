import math


def rooter():
    """
    Should receive one number and yield the square root of that 
    number. Note that you need to take the floor after doing the
    square root of the input
    """
    pass


def squarer():
    """
    Should receive one number and yield the square of that number
    """
    pass


def accumulator():
    """
    Should receive one number, should add that to the previously
    kept answer and yield that answer, the accumulator starts from
    0
    """
    pass


""" The following code cannot be modified except for debugging """


def consumer():
    while True:
        x = yield
        print("Accumulator", x)


def producer(n):
    for _ in range(n):
        x = int(input("Input number: "))
        yield x


def pipeline(prod, workers, cons):
    for num in prod:
        for i, w in enumerate(workers):
            num = w.send(num)

        cons.send(num)
    for worker in workers:
        worker.close()
    cons.close()


if __name__ == "__main__":
    """
    For example: the order in which to implement these functions
    to be order = [square, accumulate] and the numbers to be 
    nums = [1,2,3] with len n = 3

    Output: After first number (1), the output is 1, After the second
    number (2) the output is 5. After the third number (3), the output
    is 14.
    """

    order = input().strip()

    n = int(input())

    prod = producer(n)

    cons = consumer()
    next(cons)

    root = rooter()
    next(root)

    accumulate = accumulator()
    next(accumulate)

    square = squarer()
    next(square)

    pipeline(prod, eval(order), cons)

    """
    Test 1:
    - Inputs
        [square, accumulate]
        3
        1
        2
        3

    - Outpus
        1 5 14

    Test 2:
    - Inputs
        [root, square, accumulate]
        5
        3
        6
        1
        2
        3

    - Outputs
        1 5 6 7 8
    """
