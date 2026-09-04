import json

def registrar_materias():
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo:
            Horario = json.load(archivo)
    except FileNotFoundError:
        Horario = []

    for dia in dias_semana:
        print(f"\nRegistro de materias para el día {dia}:")
        
        # Pedir la cantidad de materias sin que falle por letras
        while True:
            try:
                cantidad_materias = int(input("Ingrese la cantidad de materias que desea registrar este dia: "))
                break  
            except ValueError:
                print("Error: Ingrese un valor numérico válido para la cantidad de materias.")

        # Pedir los datos de cada materia de ese día
        for i in range(cantidad_materias):
            materia = input(f"Ingrese el nombre de la materia {i+1}: ").strip().capitalize()
            if materia:
                break
            print("Error: El nombre de la materia no puede estar vacío. Por favor, ingrese un nombre válido.")
            # Pedir y validar horas
            while True:
                try:
                    Hora_inicio = int(input(f"Ingrese la hora de inicio de la materia {materia} (formato 24h, ej. 8 o 14): "))
                    Hora_fin = int(input(f"Ingrese la hora de fin de la materia {materia} (formato 24h, ej. 10 o 16): "))                    
                    if Hora_fin > Hora_inicio:
                        if 6 <= Hora_inicio <= 22 and 6 < Hora_fin <= 23:
                            cruce=False
                            for evento in Horario:
                                if evento["dia"] == dia:
                                    if max(Hora_inicio, int(evento["hora_inicio"])) < min(Hora_fin, int(evento["hora_fin"])):
                                        cruce=True
                                        print(f"Error: La materia {materia} se cruza con la materia {evento['materia']} en el horario {evento['hora_inicio']} - {evento['hora_fin']}.")
                                        break
                            if not cruce:
                                break
                        else:
                            print("Error: Las horas deben estar en el rango de 6:00 a 23:00.")
                    else:
                        print("Error: La hora de fin debe ser mayor que la hora de inicio.")
                except ValueError:
                    print("Error: Ingrese un valor numérico válido para la hora de inicio y fin.")
                while True:
                    ubicacion = input(f"Ingrese la ubicación de la materia {materia}: ").strip()
                    if ubicacion:
                        break
                    print("Error: La ubicación de la materia no puede estar vacía. Por favor, ingrese una ubicación válida.")
                Horario.append({
                "materia": materia,
                "hora_inicio": Hora_inicio,
                "hora_fin": Hora_fin,
                "ubicacion": ubicacion,
                "dia": dia
            })

    with open("Datos.json", "w", encoding="utf-8") as archivo:
        json.dump(Horario, archivo, indent=4, ensure_ascii=False)

    print("Registro de materias completado exitosamente.")