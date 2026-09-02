import json
from Registro import registrar_materias
from Visualizar import visualizar_horario
from Modificaciones import modificar_horario
from Eliminar_Materias import eliminar_materia
from Reporte import generar_reporte

while True:
    print("==============Bienvenido, selecciona la opcion que desees ejecutar: ===========================")
    opcion=input("\n Ingrese la opcion: \n 1. Registrar materias \n 2. Visualizar Horario \n 3. Modificar Horario \n 4. Eliminar materia \n 5. Generar reporte \n 6. Salir  \n")
    if opcion == "1":
        registrar_materias()
    elif opcion == "2":
        from Visualizar import visualizar_horario
        visualizar_horario()
    elif opcion == "3":
        from Modificar import modificar_horario
        modificar_horario()
    elif opcion == "4":
        from Eliminar_Materias import eliminar_materia
        eliminar_materia()
    elif opcion == "5":
        from Reporte import generar_reporte
        generar_reporte()
    elif opcion == "6":
        print("Saliendo del programa...")
        break