while True:
    def calcular_salario_neto(salario_bruto):
        impuestos = (salario_bruto // 1000) * 0.7
        salario_neto = salario_bruto - impuestos
        return salario_neto, impuestos

    if __name__ == "__main__":
        salario_bruto = float(input("Ingrese el salario bruto: "))
        salario_neto, impuestos = calcular_salario_neto(salario_bruto)
        print(f"El salario bruto es: {salario_bruto:,.2f}")
        print(f"El impuesto aplicado es: {impuestos:,.2f}")
        print(f"El salario neto después de impuestos es: {salario_neto:,.2f}")