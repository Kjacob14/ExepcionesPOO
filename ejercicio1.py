def division(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero."


print("Caso correcto:", division(10, 2))
print("Caso error:", division(10, 0))