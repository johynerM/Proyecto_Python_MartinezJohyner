import json
def modificar_horario():
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo:
            Horario = json.load(archivo)
        materia_a_modificar = input("Ingrese el nombre de la materia que desea modificar: ").strip()
        materia_encontrada = False
        for evento in Horario:
            if evento["materia"].capitalize() == materia_a_modificar.capitalize():
                materia_encontrada = True
                print(f"\nMateria encontrada: {evento['materia']} el {evento['dia']} de {evento['hora_inicio']}:00 a {evento['hora_fin']}:00 en {evento['ubicacion']}")
                print("(Presione Enter en cualquier campo si no desea cambiar su valor)\n")
                # 1. Validar Día
                while True:
                    Nuevo_Dia = input(f"Ingrese el nuevo día (si no desea cambiarlo presione Enter): ").strip().capitalize()
                    if Nuevo_Dia == "" or Nuevo_Dia in dias_semana:
                        break
                    print(f"Error: Ingrese un día válido de la semana ({', '.join(dias_semana)})")
                # 2. Validar Nombre
                Nuevo_Nombre = input(f"Ingrese el nuevo nombre para la materia (si no desea cambiarlo presione Enter): ").strip().capitalize()
                # Definir día a evaluar para los cruces
                dia_evaluar = Nuevo_Dia if Nuevo_Dia != "" else evento["dia"]
                # 3. Validar Horas y Cruces
                while True:
                    try:
                        str_ini = input(f"Ingrese la nueva hora de inicio (si no desea cambiarlo presione Enter): ").strip()
                        str_fin = input(f"Ingrese la nueva hora de fin (si no desea cambiarlo presione Enter): ").strip()
                        # Manejo de cadenas vacías (Enter)
                        h_inicio = int(str_ini) if str_ini != "" else int(evento["hora_inicio"])
                        h_fin = int(str_fin) if str_fin != "" else int(evento["hora_fin"])
                        if h_fin <= h_inicio:
                            print("Error: La hora de fin debe ser mayor que la hora de inicio. Intente nuevamente.")
                            continue
                        if not (6 <= h_inicio <= 22 and 6 < h_fin <= 23):
                            print("Error: Las horas deben estar en el rango de 6:00 a 23:00. Intente nuevamente.")
                            continue
                        # Validar cruce de horario (excluyendo la propia materia que se edita)
                        cruce = False
                        for otro_evento in Horario:
                            if otro_evento != evento and otro_evento["dia"].capitalize() == dia_evaluar.capitalize():
                                if max(h_inicio, int(otro_evento["hora_inicio"])) < min(h_fin, int(otro_evento["hora_fin"])):
                                    print(f"Error: La nueva hora se cruza con '{otro_evento['materia']}' en el horario {otro_evento['hora_inicio']}:00 - {otro_evento['hora_fin']}:00.")
                                    cruce = True
                                    break
                        if not cruce:
                            break
                    except ValueError:
                        print("Error: Ingrese un valor numérico válido para la hora de inicio y fin.")
                # 4. Validar Ubicación
                Nueva_Ubicacion = input("Ingrese la nueva ubicación (si no desea cambiarlo presione Enter): ").strip()
                # Aplicar los cambios
                if Nuevo_Dia != "":
                    evento["dia"] = Nuevo_Dia
                if Nuevo_Nombre != "":
                    evento["materia"] = Nuevo_Nombre                
                evento["hora_inicio"] = h_inicio
                evento["hora_fin"] = h_fin
                if Nueva_Ubicacion != "":
                    evento["ubicacion"] = Nueva_Ubicacion
                # Guardar en archivo
                with open("Datos.json", "w", encoding="utf-8") as archivo:
                    json.dump(Horario, archivo, indent=4, ensure_ascii=False)
                print("\n¡Materia modificada exitosamente!")
                return
        if not materia_encontrada:
            print("\nMateria no encontrada.")
    except FileNotFoundError:
        print("\nNo se encontró el archivo de datos. Asegúrese de registrar materias primero.")