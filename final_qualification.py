while True:
  calificacion = float(input("Introduce una calificación (1-5):"))

  if calificacion < 1:
    print("La nota mínima es 1, por favor, intenta nuevamente procurando escribir con los dedos mientras piensas en simultáneo")
  elif 3<=calificacion <=3.9:
    print("Su calificación es básica")
  elif 4<=calificacion <= 4.5:
    print("Su calificación es alta, pero podría ser mejor. Esfuércese más mijo")
  elif 4.5<calificacion <= 5:
    print("Su calificación es superior\nFelicidades")
  elif calificacion > 5:
    print("La calificación máxima es 5, por favor intenta nuevamente intentando usar el cerebrillo")
  else:
    print("A validar, chiquitín")