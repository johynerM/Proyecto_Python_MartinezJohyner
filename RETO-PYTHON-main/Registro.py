import json
def registrar_materias():
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado"]
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo: #Si el archivo existe, se carga el horario existente
            Horario = json.load(archivo)
    except FileNotFoundError: #Esto funciona por si el archivo no existe, para que no falle al intentar abrirlo
        Horario = []
    except json.JSONDecodeError: #Si el archivo existe pero está vacío, también se inicializa la lista vacía
        Horario = []
    for dia in dias_semana:
        print(f"\nRegistro de materias para el dia {dia}:")
        # Pedir la cantidad de materias sin que falle por letras
        while True:
            try:
                cantidad_materias = int(input("Ingrese la cantidad de materias que desea registrar este dia: "))
                break
            except ValueError:
                print("Error: Ingrese un valor numérico válido para la cantidad de materias.")
        # Con este for se pedirán los datos de cada materia de ese dia
        for i in range(cantidad_materias):
            while True:
                materia = input(f"Ingrese el nombre de la materia {i+1}: ").strip().capitalize()
                if materia:
                    break
                print("Error: El nombre de la materia no puede estar vacío. Por favor, ingrese un nombre válido.")
            # 2. Pedir las horas y hacer las validaciones correspondientes a la hora de inicio y fin, así como los cruces de horarios
            while True:
                try:
                    Hora_inicio = int(input(f"Ingrese la hora de inicio de la materia {materia} (formato 24h, ej. 8 o 14): "))
                    Hora_fin = int(input(f"Ingrese la hora de fin de la materia {materia} (formato 24h, ej. 10 o 16): "))
                    if Hora_fin > Hora_inicio:
                        if 6 <= Hora_inicio <= 22 and 6 < Hora_fin <= 23: # Validar que las horas estén en el rango de 6 a 23
                            cruce = False # Variable para verificar si hay cruce de horarios
                            for evento in Horario:
                                if evento["dia"] == dia:
                                    if max(Hora_inicio, int(evento["hora_inicio"])) < min(Hora_fin, int(evento["hora_fin"])): #Compara si hay cruce de horarios
                                        cruce = True 
                                        print(f"Error: La materia {materia} se cruza con la materia {evento['materia']} en el horario {evento['hora_inicio']}:00 - {evento['hora_fin']}:00.")
                                        break
                            if not cruce:
                                break
                        else:
                            print("Error: Las horas deben estar en el rango de 6:00 a 23:00.")
                    else:
                        print("Error: La hora de fin debe ser mayor que la hora de inicio.")
                except ValueError:
                    print("Error: Ingrese un valor numérico válido para la hora de inicio y fin.")
            # 3. Pedir y validar ubicación sin que falle por estar vacía
            while True:
                ubicacion = input(f"Ingrese la ubicación de la materia {materia}: ").strip()
                if ubicacion:
                    break
                print("Error: La ubicación de la materia no puede estar vacía. Por favor, ingrese una ubicación válida.")
            # 4. Guardar el registro de la materia en el horario
            Horario.append({
                "materia": materia,
                "hora_inicio": Hora_inicio,
                "hora_fin": Hora_fin,
                "ubicacion": ubicacion,
                "dia": dia
            })
    with open("Datos.json", "w", encoding="utf-8") as archivo: # Guardar el horario actualizado en el archivo JSON
        json.dump(Horario, archivo, indent=4, ensure_ascii=False)
    print("Registro de materias completado exitosamente.")