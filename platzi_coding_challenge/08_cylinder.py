import math

def circle_area(radio):
    return math.pi * (radio ** 2)

def cylinder_volume(area, height):
    return round(area * height, 1)

def main():
    height = float(input("Add the height of the cylinder: "))
    radio = float(input("Add the radio of the cylinder: "))

    area = circle_area(radio)
    volume = cylinder_volume(area, height)
    print(f"The volume of the cylinder is {volume}")

if __name__ == "__main__":
    main()