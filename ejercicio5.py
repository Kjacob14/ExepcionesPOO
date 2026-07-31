def sumar(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: No se pueden sumar tipos incompatibles (entero y cadena)."

print("Caso correcto:", sumar(5, 3))
print("Caso error:", sumar(5, "3"))
