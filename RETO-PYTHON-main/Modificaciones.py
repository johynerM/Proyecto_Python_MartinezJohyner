import json
def modificar_horario():
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado"]
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo: #Igual que en las otras funciones, si el archivo existe, se carga el horario existente
            Horario = json.load(archivo)
    except FileNotFoundError:
        print("\nNo se encontró el archivo de datos. Asegúrese de registrar materias primero.")
        return
    except json.JSONDecodeError:
        print("\nEl archivo 'Datos.json' está vacío o tiene un formato no válido.")
        return
    materia_a_modificar = input("Ingrese el nombre de la materia que desea modificar: ").strip()    
    coincidencias = [evento for evento in Horario if evento["materia"].capitalize() == materia_a_modificar.capitalize()] # Buscar todas las coincidencias, no solo la primera
    if not coincidencias:
        print("\nMateria no encontrada.")
        return
    if len(coincidencias) > 1:    # Si hay más de un registro con ese nombre, dejar elegir cuál modificar
        print(f"\nSe encontraron {len(coincidencias)} registros de la materia '{materia_a_modificar}':")
        for indice, ev in enumerate(coincidencias, start=1):
            print(f"{indice}. {ev['materia']} el {ev['dia']} de {ev['hora_inicio']}:00 a {ev['hora_fin']}:00 en {ev['ubicacion']}")
        while True:
            try:
                seleccion = int(input(f"\n¿Cuál desea modificar? (1-{len(coincidencias)} ): "))
                if 1 <= seleccion <= len(coincidencias):
                    break
                print(f"Error: Ingrese un número entre 1 y {len(coincidencias)}.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")
        evento = coincidencias[seleccion - 1]
    else:
        evento = coincidencias[0]
    print(f"\nMateria encontrada: {evento['materia']} el {evento['dia']} de {evento['hora_inicio']}:00 a {evento['hora_fin']}:00 en {evento['ubicacion']}")
    print("(Presione Enter en cualquier campo si no desea cambiar su valor)\n")
    while True:     # Validar el Dia 
        Nuevo_Dia = input("Ingrese el nuevo dia (si no desea cambiarlo presione Enter): ").strip().capitalize()
        if Nuevo_Dia == "" or Nuevo_Dia in dias_semana:
            break
        print(f"Error: Ingrese un dia válido de la semana ({', '.join(dias_semana)})")
    Nuevo_Nombre = input("Ingrese el nuevo nombre para la materia (si no desea cambiarlo presione Enter): ").strip().capitalize()     # Validar el Nombre
    dia_evaluar = Nuevo_Dia if Nuevo_Dia != "" else evento["dia"]
    while True:     # Validar Horas y Cruces
        try:
            str_ini = input("Ingrese la nueva hora de inicio (si no desea cambiarlo presione Enter): ").strip()
            str_fin = input("Ingrese la nueva hora de fin (si no desea cambiarlo presione Enter): ").strip()
            h_inicio = int(evento["hora_inicio"]) if str_ini == "" else int(str_ini) #Con esto se permite que si el usuario no ingresa nada, se mantenga el valor anterior
            h_fin = int(evento["hora_fin"]) if str_fin == "" else int(str_fin)
            if h_fin <= h_inicio:
                print("Error: La hora de fin debe ser mayor que la hora de inicio. Intente nuevamente.")
                continue
            if not (6 <= h_inicio <= 22 and 6 < h_fin <= 23):
                print("Error: Las horas deben estar en el rango de 6:00 a 23:00. Intente nuevamente.")
                continue
            cruce = False #Con esto podemos verificar si hay cruce de horarios con otras materias
            for otro_evento in Horario:
                if otro_evento is not evento and otro_evento["dia"].capitalize() == dia_evaluar.capitalize(): #Verificar que sea el mismo día y que no sea el mismo evento
                    if max(h_inicio, int(otro_evento["hora_inicio"])) < min(h_fin, int(otro_evento["hora_fin"])):
                        print(f"Error: La nueva hora se cruza con '{otro_evento['materia']}' en el horario {otro_evento['hora_inicio']}:00 - {otro_evento['hora_fin']}:00.")
                        cruce = True
                        break
            if not cruce:
                break
        except ValueError:
            print("Error: Ingrese un valor numérico válido para la hora de inicio y fin.")
    Nueva_Ubicacion = input("Ingrese la nueva ubicación (si no desea cambiarlo presione Enter): ").strip()
    if Nuevo_Dia != "":     # Aplicar los cambios realizados por el usuario al evento seleccionado
        evento["dia"] = Nuevo_Dia
    if Nuevo_Nombre != "":
        evento["materia"] = Nuevo_Nombre
    evento["hora_inicio"] = h_inicio
    evento["hora_fin"] = h_fin
    if Nueva_Ubicacion != "":
        evento["ubicacion"] = Nueva_Ubicacion
    with open("Datos.json", "w", encoding="utf-8") as archivo:     # Guardar en el archivo JSON los cambios realizados
        json.dump(Horario, archivo, indent=4, ensure_ascii=False)
    print("\n¡Materia modificada exitosamente!")