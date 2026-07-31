def vender(inventario, medicamento, cantidad):
    try:
        if cantidad > inventario[medicamento]:
            raise Exception("No hay suficiente stock para realizar la venta.")
        inventario[medicamento] -= cantidad
        print(f"Venta confirmada. Stock restante de {medicamento}: {inventario[medicamento]}")
    except Exception as e:
        print(f"Error en la transacción: {e}")

inventario_actual = {"paracetamol": 50, "ibuprofeno": 20}
print("Caso correcto:")
vender(inventario_actual, "paracetamol", 10)
print("Caso error:")
vender(inventario_actual, "ibuprofeno", 30)