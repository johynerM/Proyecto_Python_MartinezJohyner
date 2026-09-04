import json
def visualizar_horario():
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo: #Si el archivo existe, se carga el horario existente
            Horario = json.load(archivo)         
        if not Horario:
            print("\nNo hay materias registradas en el horario.")
            return
        dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado"]
        Ancho_Hora = 14 #Con esto ponemos los anchos de las columnas para que se vea más ordenado
        Ancho_Columna = 22
        encabezado = f"{'Hora':<{Ancho_Hora}} | " + " | ".join([f"{dia:<{Ancho_Columna}}" for dia in dias_semana]) #Con el :< alineamos a la izquierda
        separador = "=" * len(encabezado) 
        print("\n" + separador)
        print(encabezado)
        print(separador)
        for hora in range(6, 23):
            hora_texto = f"{hora}:00 - {hora+1}:00"
            fila = f"{hora_texto:<{Ancho_Hora}} | "
            for dia in dias_semana:
                materia_encontrada = "Libre"
                for evento in Horario:
                    if evento["dia"].capitalize() == dia.capitalize(): #Asegurarse que sea el mismo día, sin importar mayúsculas o minúsculas
                        try:
                            H_inicio = int(evento["hora_inicio"])
                            H_fin = int(evento["hora_fin"])
                        except (ValueError, TypeError):
                            continue
                        if H_inicio <= hora < H_fin: 
                            texto_info = f"{evento['materia']} ({evento['ubicacion']})"
                            if len(texto_info) > Ancho_Columna: # Acomodar si supera el ancho de la columna para no desalinear la tabla
                                materia_encontrada = texto_info[:Ancho_Columna - 3] + "..."
                            else:
                                materia_encontrada = texto_info
                            break
                fila += f"{materia_encontrada:<{Ancho_Columna}} | "
            print(fila)
        print("=" * len(encabezado) + "\n")
    except FileNotFoundError:
        print("\nNo se encontró el archivo 'Datos.json'. Asegúrese de registrar materias primero.")
    except json.JSONDecodeError:
        print("\nEl archivo 'Datos.json' está vacío o tiene un formato no válido.")