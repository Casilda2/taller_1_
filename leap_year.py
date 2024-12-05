while True:
    def es_bisiesto(anio):
        if (anio % 4 == 0):
            if (anio % 100 == 0):
                if (anio % 400 == 0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    if __name__ == "__main__":
        anio = int(input("Ingrese un año: "))
        if es_bisiesto(anio):
            print(f"El año {anio} es bisiesto.")
        else:
            print(f"El año {anio} no es bisiesto.")