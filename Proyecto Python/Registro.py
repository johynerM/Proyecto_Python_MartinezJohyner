import json
def registrar_materias():
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

    try: 
        with open("Datos.json", "r", encoding="utf-8") as archivo:
            Horario = json.load(archivo)
    except FileNotFoundError:
        Horario = []

    for dia  in dias_semana:
        print(f"Registro de materias para el día {dia}:")
        cantidad_materias =int(input("Ingrese la cantidad de materias que desea registrar este dia: "))
        for i in range(cantidad_materias):
            materia = input(f"Ingrese el nombre de la materia {i+1}: ").capitalize()
            Hora_inicio = input(f"Ingrese la hora de inicio de la materia {materia} ")
            Hora_fin = input(f"Ingrese la hora de fin de la materia {materia} ")
            ubicacion = input(f"Ingrese la ubicación de la materia {materia} ")
            Horario.append({
                "materia": materia,
                "hora_inicio": Hora_inicio,
                "hora_fin": Hora_fin,
                "ubicacion": ubicacion,
                "dia": dia
            })
    with open("Datos.json", "w", encoding="utf-8") as archivo:
        json.dump(Horario, archivo, indent=4, ensure_ascii=False)
print ("Registro de materias completado exitosamente.")