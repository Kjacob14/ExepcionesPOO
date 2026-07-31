def obtener_color(indice):
    colores = ["rojo", "verde", "azul"]
    try:
        return colores[indice]
    except IndexError:
        return f"Error: Índice inválido, Solo hay {len(colores)} colores disponibles."

print("Caso correcto:", obtener_color(1))
print("Caso error:", obtener_color(5))  