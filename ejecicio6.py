def registrar_edad(edad):
    try:
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        print(f"Edad registrada correctamente: {edad}")
    except ValueError as e:
        print(f"Error de validación: {e}")

print("Caso éxito:")
registrar_edad(21)
print("Caso error:")
registrar_edad(-5)