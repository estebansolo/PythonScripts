# Generators (yield)

## What are generators?

Generator functions allow you to declare a function that behaves like an iterator.
These are objects that you can loop over like a list. However, unlike lists, these iterators do not store their contents in memory

## Create a generator

```python
def my_generator():
    for i in range(5):
        yield i

# The generator returns an object but it does not start.
my_gen = my_generator()

# Once the function yields, the function is paused and the control
# is transferred to the caller.
print(next(my_gen)) # 1
print(next(my_gen)) # 2
print(next(my_gen)) # 3
print(next(my_gen)) # 4
print(next(my_gen)) # 5

# Finally, when the iterator ends, StopIteration is raised automatically.
```

We can use these generator with for loops to iterate over each object

```python
def my_generator():
    for i in range(5):
        yield i

# This for will print all values from 0 to 5
for i in my_generator():
    print(i)
```

## If you want to solve the exercises without help, please do not continue.

While looking for how to solve these exercises I found the `send` method that the generators have, this method allows to pass to the generator (which is waiting) a new value which can manipulate.

```python
def my_generator():
    accumulator = 0
    while True:
        num = yield accumulator
        accumulator += num

# We initialize the generator
my_gen = my_generator()
next(my_gen)

for i in range(2, 5):
    # This will send number from 2 to 5 (2, 3, 4) to the generator
    # and then it will print the accumulator saved in the function
    acc = my_gen.send(i)
    print(acc)

    # The outout will be 2 5 9
```

We don't have problems if we do not break the generator because it does not store its values in memory, we can use it every time we need passing values (if we have to) and expect a processed result.
