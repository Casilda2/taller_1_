while True:
    def determinar_orden_y_iguales(numero1, numero2, numero3):
        if numero1 == numero2 == numero3:
            return {"mayor": numero1, "medio": numero1, "menor": numero1, "iguales": True}
    
        if numero1 >= numero2 and numero1 >= numero3:
            mayor = numero1
            medio = max(numero2, numero3)
            menor = min(numero2, numero3)
        elif numero2 >= numero1 and numero2 >= numero3:
            mayor = numero2
            medio = max(numero1, numero3)
            menor = min(numero1, numero3)
        else:
            mayor = numero3
            medio = max(numero1, numero2)
            menor = min(numero1, numero2)
        iguales = numero1 == numero2 or numero2 == numero3 or numero1 == numero3
        return {"mayor": mayor, "medio": medio, "menor": menor, "iguales": iguales}

    if __name__ == "__main__":
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        numero3 = float(input("Ingrese el tercer número: "))
    
        resultado = determinar_orden_y_iguales(numero1, numero2, numero3)
    
        if resultado["iguales"] and resultado["mayor"] == resultado["medio"] == resultado["menor"]:
            print("Los tres números son iguales.")
        else:
            print(f"Mayor: {resultado['mayor']}")
            print(f"Medio: {resultado['medio']}")
            print(f"Menor: {resultado['menor']}")
            if resultado["iguales"]:
                print("Hay números iguales.")