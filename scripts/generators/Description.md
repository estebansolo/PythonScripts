# Square Accumulate Root

Arthur needs to perform 3 operations on an input - squaring a number, taking square root of a number or
sum of the input numbers. But the order of these operations is not known before hand. Arthur realized it
to be a perfect situation to implement it using co-routines and producer-filter-consumer pattern.

Arthur has implemented the producer, consumer and the pipeline and needs help to setup accumulator (for
summing the input), squarer (for squaring the input), and rooter (for taking square root of a number)
co-routines.

The **accumulator** should receive one number, should add that to the previuosly kept answer and yield
that answer. The accumulator starts from 0.

The **squarer** should receive one numberand yield the square of that number.

The **rooter** should receive one number and yield the square root of that number. Note that you need to
take the floor after doing the square root of the input.

Take for example, the order in which to implement these functions to be *order = [square, accumulate]* and
the numbers to be *nums = [1, 2, 3]* with length *n = 3*. The complete function then is
*accumulate(square(nums))*. After the first number (1), the output is 1. After the second number (2), the
output is 5. After the third number (3), the output is 14.

### Functions Description

Complete the co-routines *accumulator*, *squarer*, and *rooter* in the editor.

These co-routines do not have any input and communicate completely through sub-routine pipeline.

### Constraints

    - 1 <= n <= 10^5
    - 1 <= nums <= 10^5 (where 0 <= i <= n)
    
### Input Format For Custom Testing

The first line contains a string, order, describing the order inwhich to perform the operations.
The next line contains an integer, n, denoting the number of elements in nums
Each line i of the n subsequent lines (where 0 <= i <= n) contains an integer describing nums.

### Sample 0

```
[square, accumulate]
3
1
2
3
```

**sample output**

```
1
5
14
```

**Explanation**

The order of the function shows that we need to square a number and then accumulate the result.
So, first we have 1, we get 1 as answer. Then we have 2 (making nums as [1, 2]), we get 5 as answer.
Then at last, we have 3 (making nums [1, 2, 3]), we get 14 as answer.

### Sample 1

```
[root, square, accumulate]
5
3
6
1
2
3
```

**sample output**

```
1
5
6
7
8
```

**Explanation**

The order of the function shows that we need to take square root of the input number first, then again
square the number and then accumulate the numbers. So first we have 3 which goes through the transformation
as *root (3) -> 1, square (1) -> 1, accumulate (1) -> 1*, then, we get 6 which goes through tha transformation
as *root (6) -> 2, square (2) -> 4, accumulate (4) -> 5*, and so for the rest of the numbers.




# Non-primes Generator

Given an integer k, print the first k non-prime positive integers, each on a new line. For example
if k = 10, the output would be:
    
```
1
4
6
8
9
10
12
14
15
16
```

### Functions Description

Complete the function *manipulate_generator* in the editor. The function must manipulate the
generator function so that the first k non-prime positive integers are printed, each on a separated
line.

manipulate_generator has the following parameters.
    
    g: a generator
    n: an integer

### Constraints

    - 1 <= k <= 10^5
    
### Input Format For Custom Testing

Input will be processed as follows and passed to the function.
The only line contains a single integer k, the number of non-primes to print.

### Sample 0

```
12
```

**sample output**

```
1
4
6
8
9
10
12
14
15
16
18
20
```

**Explanation**

The output contains the first 12 non-prime positive integers.