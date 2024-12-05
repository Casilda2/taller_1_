while True:
    def calcular_imc(peso, altura):
        imc = peso / (altura ** 2)
        if imc < 18.5:
            categoria = "Bajo peso"
        elif 18.5 <= imc < 24.9:
            categoria = "Peso normal"
        elif 25 <= imc < 29.9:
            categoria = "Sobrepeso"
        else:
            categoria = "Obesidad"
        return imc, categoria

    if __name__ == "__main__":
        peso = float(input("Ingrese su peso (kg): "))
        altura = float(input("Ingrese su altura (m): "))
    
        imc, categoria = calcular_imc(peso, altura)
        print(f"Tu IMC es: {imc:.2f}")
        print(f"Categoría: {categoria}")