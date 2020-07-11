def print_matriz(matriz):
    print(*matriz, sep="\n")

def matriz_bordes(length):
    # Se utiliza el tamaño de la matriz para saber el final de la misma
    matriz = []
    for key_fila in range(length):
        if key_fila == 0 or key_fila == (length - 1):
            # Si es la primer o ultima fila, poner cada valor en 0
            fila = ["0"] * length
        else:
            # Si no es ni la primera ni la ultima fila, solo poner
            # la columna 0 y la ultima
            fila = ["_"] * length
            fila[0] = "0"
            fila[length - 1] = "0"
            
        matriz.append(fila)

    print_matriz(matriz)


def diagonal_principal(length):
    matriz = []
    # Contador para saber que numero sigue en la secuencia
    contador = 1
    for key_fila in range(length):
        fila = ["_"] * length
        for key_columna in range(length):
            if key_fila == key_columna:
                # Si ambas posiciones son las mismas es donde va la diagonal
                fila[key_columna] = str(contador)
                # Se suma para tener el siguiente valor
                contador += 1

        # Agregar fila de valores
        matriz.append(fila)

    print_matriz(matriz)


def matriz_llena(length):
    matriz = []
    for key_fila in range(length):
        fila = ["_"] * length
        for key_columna in range(length):
            # El valor es la suma de las indices de la matriz
            fila[key_columna] = key_fila + key_columna

        matriz.append(fila)

    print_matriz(matriz)


def diagonales(length):
    matriz = []
    for key_fila in range(length):
        fila = ["_"] * length
        for key_columna in range(length):
            if key_fila == key_columna:
                # Si ambas posiciones son las mismas es donde va la diagonal
                fila[key_columna] = "0"
        
        # Segunda Diagonal
        fila[length - 1 - key_fila] = "0"

        matriz.append(fila)

    print_matriz(matriz)


def main():
    divisor = "*" * 50

    print(divisor, "Matrices".center(50), divisor, sep="\n")

    constante_matriz = int(input("Ingrese el tamaño de la matriz [>=3]: "))
    if constante_matriz < 3:
        constante_matriz = 3

    while True:
        menu = (
            "A. Diagonales en 0",
            "B. Bordes en 0",
            "C. Matriz Llena",
            "D. Diagonal Principal",
            divisor
        )

        print(*menu, sep="\n")

        
        opcion = input("Seleccione el tipo de matriz: ")
        if opcion.lower() not in ["a", "b", "c", "d"]:
            continue

        if opcion.lower() == "a":
            diagonales(constante_matriz)
        elif opcion.lower() == "b":
            matriz_bordes(constante_matriz)
        elif opcion.lower() == "c":
            matriz_llena(constante_matriz)
        elif opcion.lower() == "d":
            diagonal_principal(constante_matriz)

        break

if __name__ == "__main__":
    main()