def convertir_edad():
    while True:
        try:
            return int(input("Introduce tu edad: "))
        except ValueError:
            print("Error: Entrada no válida, escribe un número entero.")

print("Edad ingresada:", convertir_edad())