import re

def validar_contrasena(contrasena):
    longitud_valida = len(contrasena) >= 8
    tiene_mayuscula = any(char.isupper() for char in contrasena)
    tiene_minuscula = any(char.islower() for char in contrasena)
    tiene_numero = any(char.isdigit() for char in contrasena)
    tiene_especial = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena))

    if all([longitud_valida, tiene_mayuscula, tiene_minuscula, tiene_numero, tiene_especial]):
        return True, "La contraseña es válida."
    else:
        errores = []
        if not longitud_valida:
            errores.append("Debe tener al menos 8 caracteres.")
        if not tiene_mayuscula:
            errores.append("Debe incluir al menos una letra mayúscula.")
        if not tiene_minuscula:
            errores.append("Debe incluir al menos una letra minúscula.")
        if not tiene_numero:
            errores.append("Debe incluir al menos un número.")
        if not tiene_especial:
            errores.append("Debe incluir al menos un carácter especial.")
        return False, "\n".join(errores)

if __name__ == "__main__":
    contrasena = input("Ingrese su contraseña: ")
    valida, mensaje = validar_contrasena(contrasena)
    print(mensaje)