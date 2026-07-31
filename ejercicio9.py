class StockInsuficienteError(Exception):
    pass
def vender(inventario, medicamento, cantidad):
    try:
        stock_actual = inventario[medicamento]
        if cantidad > stock_actual:
            faltante = cantidad - stock_actual
            raise StockInsuficienteError(f"Stock insuficiente de {medicamento}. Faltan {faltante} piezas.")
        inventario[medicamento] -= cantidad
        print(f"Venta de {medicamento} exitosa.")
    except StockInsuficienteError as e:
        print(f"Excepción Personalizada -> {e}")

inventario_farmacia = {"paracetamol": 50, "ibuprofeno": 20}
print("Caso correcto:")
vender(inventario_farmacia, "ibuprofeno", 5)
print("Caso de error:")
vender(inventario_farmacia, "ibuprofeno", 20) 