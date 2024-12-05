while True:
    edad = int(input("¿Cuántos años tienes?: "))

    if 0 <= edad < 18:
        print("Ya casi... Ya casi...")
    elif 18>= edad <= 60:
        print("No olvides ejercer tu derecho al voto")
    elif 60 >edad <= 90:
        print("¿Ya sabes a quién dejar tu herencia? \nYo... no tendría ningún problema")
    elif 90>edad<=100 :
        print("Wow")
    else:
        print("¿Okey...?")