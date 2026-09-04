import json

def visualizar_horario():
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo:
            Horario = json.load(archivo)         
        if not Horario:
            print("\nNo hay materias registradas en el horario.")
            return
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        Ancho_Hora = 14
        Ancho_Columna = 22

        encabezado = f"{'Hora':<{Ancho_Hora}} | " + " | ".join([f"{dia:<{Ancho_Columna}}" for dia in dias_semana])
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
                    if evento["dia"].capitalize() == dia.capitalize():
                        # Obtener las horas asegurando formato entero
                        try:
                            H_inicio = int(evento["hora_inicio"])
                            H_fin = int(evento["hora_fin"])
                        except (ValueError, TypeError):
                            continue
                        # Verificar si la hora actual cae en el rango de la clase
                        if H_inicio <= hora < H_fin:
                            texto_bruto = f"{evento['materia']} ({evento['ubicacion']})"
                            # Acomodar si supera el ancho de la columna para no desalinear la tabla
                            if len(texto_bruto) > Ancho_Columna:
                                materia_encontrada = texto_bruto[:Ancho_Columna - 3] + "..."
                            else:
                                materia_encontrada = texto_bruto
                            break
                fila += f"{materia_encontrada:<{Ancho_Columna}} | "
            print(fila)
        print("=" * len(encabezado) + "\n")
    except FileNotFoundError:
        print("\nNo se encontró el archivo 'Datos.json'. Asegúrese de registrar materias primero.")
    except json.JSONDecodeError:
        print("\nEl archivo 'Datos.json' está vacío o tiene un formato no válido.")