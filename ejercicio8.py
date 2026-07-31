def registrar_nota(nota):
    try:
        if nota < 0 or nota > 10:
            raise ValueError("La calificación está fuera de rango.")
        print(f"calificacion registrada: {nota}")
    except ValueError as e:
        print(f"Error: {e} (Debe estar entre 0 y 10).")
        
print("Caso correcto:")
registrar_nota(8.5)

print("Caso error:")
registrar_nota(11.2)