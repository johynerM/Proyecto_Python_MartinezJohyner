# -----------------EJERCICIO NUMERO 1------------------
# tarifa = {"moto": 1500, "carro": 3000, "bus": 5000}
# vehiculo = input("ingrese el tipo de vehiculo (moto, carro, bus): ").lower().strip()
# if vehiculo in tarifa:
#     horas = int(input("Ingrese la cantidad de horas que estara el vehiculo: "))
#     pagar = tarifa[vehiculo] * horas
#     print(f"el valor a pagar sera de: {pagar}")
# else:
#     print("no se reconoce este tipo de vehiculo")
    
#----------------EJERCICIO NUMERO 2------------------
# nombre = input("Ingrese su nombre ")
# edad = input("ingrese su edad ")
# semestre = input("ingrese en que semestre se encuentra ")
# programa = input("ingrese el programa academico en el que esta cursando  ")

# info_estudiante = {"nombre": nombre, "edad": edad, "semestre": semestre, "programa": programa}
# print(f"el estudiante {info_estudiante['nombre']} tiene {info_estudiante['edad']} años, se encuentra en el semestre {info_estudiante['semestre']} y esta cursando el programa academico de {info_estudiante['programa']}")

#----------------EJERCICIO NUMERO 3------------------

# inventario={"Cuaderno": 20, "Lapicero": 35, "Borrador": 15, "Marcador": 10}

# while True:
#     opcion = int(input("Ingrese la opcion que desee realizar: (1) Vender producto (2) Reabastecer producto (3) Salir "))
#     print(f"el inventario actual es: {inventario}")
#     if opcion == 1:
#         compra=input("Ingrese el producto que desea comprar🤑: ").capitalize().strip()
#         if compra in inventario:
#             cantidad_compra=int(input("Cuantos elementos desea comprar🧐: "))
#             if cantidad_compra <= inventario[compra]:
#                 inventario[compra] -= cantidad_compra
#                 print(f"🤩Compra realizada con exito, el inventario actual es: {inventario}")
#             else:
#                 print("😔No hay stock suficiente en el inventario para realizar la compra.")
#         else:
#             print("😕El producto no esta disponible en la tienda por el momento")
#     elif opcion == 2:
#         producto = input("ingrese el producto que desea reabastecer: ").capitalize().strip()
#         if producto in inventario:
#             cantidad_reabastecer=int(input("Ingrese cuanto desea reabastecer: "))
#             inventario[producto] += cantidad_reabastecer
#             print(f"😁Reabastecimiento realizado con exito, el inventario actual es: {inventario}")
#     elif opcion == 3:
#         print("Gracias por usar el programa🤩 ")
#         break
#------------------EJERCICIO NUMERO 4------------------
