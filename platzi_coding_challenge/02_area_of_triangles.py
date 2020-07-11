import math
from functools import reduce


def triangle_type(side_a, side_b, side_c):
    if side_a == side_b == side_c:
        return "equilateral"
    elif side_a != side_b != side_c:
        return "scalene"
    
    return "isosceles"

def area_of_triangle(*args):
    """
    Using Heron's formula
    """

    semiperimeter = sum(args) / 2
    calc_by_side = [(semiperimeter - arg) for arg in args]
    total_sides = reduce(lambda carried, arg: carried * arg, calc_by_side)
    
    return math.sqrt(semiperimeter * total_sides)

def main():
    sides = []
    for side in range(1, 4):
        sides.append(float(input(f"Add the {side} side of the triangle: ")))

    ttype = triangle_type(*sides)
    area = area_of_triangle(*sides)
    print(f"The area of the triangle {ttype.title()} is {round(area, 2)}")

if __name__ == "__main__":
    main()