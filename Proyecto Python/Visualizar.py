import json
def visualizar_horario():
    try:
        with open("Datos.json","r", encoding="utf-8") as archivo:
            Horario =json.load(archivo)
            if not Horario:
                print("No hay materias registradas.")
                return
            dias_semana =["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
            print("\n==============Horario de la Semana=====================")
            for dia in dias_semana:
                print(f"\n----{dia.upper()} ------")
                materias_dia = [evento for evento in Horario if evento["dia"].capitalize() == dia.capitalize()]
                
                if materias_dia:
                    for m in materias_dia:
                        print(f"Materia: {m['materia']}, Hora: {m['hora_inicio']} - {m['hora_fin']}, Ubicación: {m['ubicacion']}") 
                else:
                    print("No hay materias registradas para este día.")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Asegúrese de registrar materias primero.")
        return