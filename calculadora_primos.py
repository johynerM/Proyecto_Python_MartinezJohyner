while True:
    numero=int(input("ingrese un numero para detectar si es primo o no: "))
    contador_de_numero = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador_de_numero += 1
    if contador_de_numero == 2:
        print("este numero es primo")
    else:
        print("este numero no es primo")
