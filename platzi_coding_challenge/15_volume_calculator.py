import math

def cylinder(radius, height):
    area = math.pi * (radius ** 2)
    return area * height


def cube(side):
    return side ** 3


def sphere(radius):
    return (4 * (math.pi) * (radius**3)) / 3


def main():
    print("Volume Calculator".center(50))
    print("*" * 50)

    figures = {
        1: "Cylinder",
        2: "Cube",
        3: "Sphere"
    }

    for key, ftype in figures.items():
        print(f"{key}. {ftype}")

    option = int(input("Select an option: "))
    print("*" * 50)
    if option in figures:
        if option == 1:
            radius = float(input("Insert the radius: "))
            height = float(input("Insert the height: "))
            volume = cylinder(radius, height)
        elif option == 2:
            side = float(input("Insert the size of one side: "))
            volume = cube(side)
        elif option == 3:
            radius = float(input("Insert the radius: "))
            volume = sphere(radius)
        print(f"The volume for a {figures[option]} is {round(volume, 1)}")
    else:
        print("Bad Option")
    

if __name__ == "__main__":
    main()