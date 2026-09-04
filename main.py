import json
while True:
    try:
        print("\n==================Bienvenido, selecciona la opcion que desees ejecutar: ==================")
        print("1. Registrar materias")
        print("2. Visualizar Horario")
        print("3. Modificar Horario")
        print("4. Eliminar materia")
        print("5. Generar reporte")
        print("6. Salir")
        opcion = input("\nIngrese la opcion: ").strip()
        if opcion == "1":
            from Registro import registrar_materias
            registrar_materias()
        elif opcion == "2":
            from Visualizar import visualizar_horario
            visualizar_horario()
        elif opcion == "3":
            from Modificaciones import modificar_horario
            modificar_horario()
        elif opcion == "4":
            from Eliminar_Materias import eliminar_materia
            eliminar_materia()
        elif opcion == "5":
            from reporte import generar_reporte
            generar_reporte()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("\nError: Ingrese un numero dentro del rango de opciones (1-6)")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")