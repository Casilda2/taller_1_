def calcular_precio_con_descuento(precio_original, porcentaje_descuento, condicion):
    if condicion:
        descuento = precio_original * (porcentaje_descuento / 100)
        precio_final = precio_original - descuento
    else:
        descuento = 0
        precio_final = precio_original
    return precio_final, descuento

if __name__ == "__main__":
    precio_original = float(input("Ingrese el precio original del producto: "))
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
    condicion = precio_original > 1000
    precio_final, descuento = calcular_precio_con_descuento(precio_original, porcentaje_descuento, condicion)
    print(f"Descuento aplicado: {descuento:,.2f}")
    print(f"Precio final después del descuento: {precio_final:,.2f}")