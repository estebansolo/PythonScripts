"""
A hexadecimal number is obtained from a decimal number by performing successive
divisions by 16 until it can no longer be divided.

The digits of the respective hexadecimal number are shown in the reverse direction
of calculation and correspond to the residues which are numbers between 0 and 15.
will start with the last quotient.
"""

from string import ascii_uppercase

def num_to_val(num):
    """
    Regarding hexadecimals
    
    if the value of the residue is greater than or equal to 10,
    the letters A to F are taken
    """

    if num >= 10:
        num = ascii_uppercase[num - 10]
    
    return str(num)

def dec_to_hex(decimal):
    hexadecimal = []
    while decimal > 15:
        decimal, reminder = divmod(decimal, 16)
        hexadecimal.append(num_to_val(reminder))
    
    hexadecimal.append(num_to_val(decimal))

    return "".join(hexadecimal[::-1])

if __name__ == "__main__":
    # 987462 -> F1146
    # 54968 -> D6B8

    divisor = "*" * 50
    menu = (divisor, "Decimal to Hexadecimal".center(50), divisor)
    
    print(*menu, sep="\n")

    decimal = int(input("Decimal Number: "))
    hexadecimal = dec_to_hex(decimal)

    print(f"{decimal} is equals to {hexadecimal}")
    print(divisor)