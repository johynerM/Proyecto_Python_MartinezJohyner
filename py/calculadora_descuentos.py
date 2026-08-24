while True:
    
    precio = float(input("Ingresa el precio del producto😝: "))
    #esta parte es para salir del programa

    if precio==0:
        print("Gracias por usar el programa")
        break
    
    #selecciona la categoria para aplicar el descuento
    
    print("escoja una de las categorias disponibles: ")
    categoria =input("electronica, ropa, hogar o alimentos ").strip().lower()
    if categoria=="electronica":
        descuento_aplicado=0.15
    elif categoria=="ropa":
        descuento_aplicado=0.10
    elif categoria=="hogar":
        descuento_aplicado=0.08
    elif categoria=="alimentos":
        descuento_aplicado=0.05
    else:
        print("❌❌ERROR, CATEGORIA NO VALIDA INTENTE DE NUEVO❌❌")
        continue
    descuento = precio * descuento_aplicado
    precio_final = precio - descuento
    print(f"el descuento aplicado es: {descuento_aplicado*100}%")
    print(f"el monto que se desconto fue de: {descuento}")
    print(f"el precio final del producto es: {precio_final}")
    
    