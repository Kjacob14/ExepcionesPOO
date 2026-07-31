def inventarioMed(medicamento):
    inventario = {"paracetamol": 50, "ibuprofeno": 20}
    try:
        return inventario[medicamento]
    except KeyError:
        return f"Error: El medicamento '{medicamento}' no está registrado."

print("Inventario de paracetamol:", inventarioMed("paracetamol"))
print("Inventario de aspirina:", inventarioMed("aspirina"))    