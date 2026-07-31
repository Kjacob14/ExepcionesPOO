def validar_correo(correo):
    try:
        if "@" not in correo:
            raise ValueError("Falta el símbolo '@' en la dirección.")
        print(f"El correo '{correo}' tiene un formato válido.")
    except ValueError as e:
        print(f"Error de formato: {e}")

print("Caso correcto:")
validar_correo("rober@gmail.com")
print("Caso de error:")
validar_correo("jacobgmail.com.com")