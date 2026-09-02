import json

def modificar_horario():
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo:
            Horario = json.load(archivo)
            materia_a_modificar = input("Ingrese el nombre de la materia que desea modificar: ")
            materia_encontrada = False
            for evento in Horario:
                if evento["materia"].capitalize() == materia_a_modificar.capitalize():
                    materia_encontrada = True
                    print(f"Materia encontrada: {evento['materia']} en {evento['dia']} de {evento['hora_inicio']} a {evento['hora_fin']} en {evento['ubicacion']}")
                    Nuevo_Nombre = input("Ingrese el nuevo nombre para la materia (si no desea cambiarlo presione Enter): ")
                    Nueva_Hora_inicio = input("Ingrese la nueva hora de inicio (si no desea cambiarlo presione Enter): ")
                    Nueva_Hora_fin = input("Ingrese la nueva hora de fin (si no desea cambiarlo presione Enter): ")
                    Nueva_Ubicacion = input("Ingrese la nueva ubicación (si no desea cambiarlo presione Enter): ")
                    Nuevo_Dia = input("Ingrese el nuevo día (si no desea cambiarlo presione Enter): ")
                    if Nuevo_Dia != "":
                        evento["dia"] = Nuevo_Dia
                    if Nuevo_Nombre != "":
                        evento["materia"] = Nuevo_Nombre
                    if Nueva_Hora_inicio != "":
                        evento["hora_inicio"] = Nueva_Hora_inicio
                    if Nueva_Hora_fin != "":
                        evento["hora_fin"] = Nueva_Hora_fin
                    if Nueva_Ubicacion != "":
                        evento["ubicacion"] = Nueva_Ubicacion
                    with open("Datos.json", "w", encoding="utf-8") as archivo:
                        json.dump(Horario, archivo, indent=4, ensure_ascii=False)
                        print("Materia modificada exitosamente.")
                    return
            if not materia_encontrada:
                print("Materia no encontrada.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Asegúrese de registrar materias primero.")
        return
