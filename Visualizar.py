import json
def visualizar_horario():
    try:
        with open("Datos.json","r", encoding="utf-8") as archivo:
            Horario =json.load(archivo)
            if not Horario:
                print("No hay materias registradas.")
                return
            dias_semana =["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"]
            Ancho_Hora = 14
            Ancho_Columna = 22
            encabezado = f"{'Hora':<{Ancho_Hora}}| " + " | ".join([f"{dia:<{Ancho_Columna}}" for dia in dias_semana])
            separador = "=" * len(encabezado)
            print("\n" + separador) 
            print(encabezado)
            print(separador)
            for hora in range(6,23):
                hora_texto=f"{hora}:00 - {hora+1}:00"
                fila= f"{hora_texto :<{Ancho_Hora}}|"
                for dia in dias_semana:
                    materia_encontrada = "Libre"
                    for evento in Horario:
                        if evento["dia"].capitalize() == dia.capitalize():
                            H_inicio = int(evento["hora_inicio"].split(":")[0] if ":" in str(evento["hora_inicio"])else int(evento["hora_inicio"]))
                            H_fin = int(evento["hora_fin"].split(":")[0] if ":" in str(evento["hora_fin"])else int(evento["hora_fin"]))
                            if H_inicio <= hora < H_fin:
                                materia_encontrada = evento["materia"]
                                materia_encontrada = f"{evento['materia']} ({evento['ubicacion']})"
                                break
                    fila += f"{materia_encontrada:<{Ancho_Columna}}"
                print(fila)
            print("=" *len(encabezado),"\n")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Asegúrese de registrar materias primero.")
        return