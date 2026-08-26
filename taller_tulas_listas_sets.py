# #  1 Lista de mercado
# mercado =["leche", "pan", "huevos"]
# nuevo_producto = input("Ingrese un nuevo producto para agregar a la lista de mercado: ").lower().strip()
# if nuevo_producto in mercado:
#     print("El producto ya se encuentra en la lista de mercado.")
# else:
#     mercado.append(nuevo_producto)

# producto_urgente = input("Ingrese un producto urgente para agregar al inicio de la lista de mercado: ")
# mercado.insert(0, producto_urgente)

# eliminar = input("si desea eliminar un producto escribalo de lo contrario presione enter: ")
# if eliminar in mercado:
#     mercado.remove(eliminar)

# print(sorted(mercado))

##---------------------EJERCICIO NUMERO 2-----------------

# inventario = [("Camiseta", 25000, 10), ("Short", 150000, 3), ("Camisilla", 10000, 10), ("Pantalon", 45000, 8)]
# print(f"este es el catalogo actual: {inventario}")
# for i in range(len(inventario)):
#     nombre, precio, disponibilidad = inventario[i]
#     if disponibilidad < 5:
#         recargar = input(f"el producto {nombre} con valor de {precio} no tiene disponibilidad, ingrese la cantidad a recargar del producto: ")
#         nueva_cantidad = disponibilidad + int(recargar)
#         inventario[i] = (nombre, precio, nueva_cantidad)
# print(inventario)

##---------------------EJERCICIO NUMERO 5-----------------

# pacientes=["Camilo", "Dana","Leonardo","Lucia"]
# while pacientes:
#     paciente_actual = pacientes.pop(0)
#     print(f"En este momento estamos atendiendo al paciente: {paciente_actual}")

##---------------------EJERCICIO NUMERO 6-----------------

# notas = [5.0, 4.0, 3.9, 4.8, 4.3, 3.5]
# n=len(notas)
# for i in range(n):
#     for j in range(n - 1 - i):
#         if notas[j] > notas[j + 1]:
#             notas[j], notas[j+1] = notas[j+1], notas[j]
# print("Las notas ordenadas de menor a mayor son:", notas)