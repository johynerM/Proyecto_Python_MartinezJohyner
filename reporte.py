import json
def generar_reporte():
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        if not datos:
            print("\nNo hay materias registradas para generar un reporte.")
            return
        materias_unicas = sorted(list({m["materia"].capitalize() for m in datos}))
        total_materias_unicas = len(materias_unicas)
        total_sesiones = len(datos)
        total_horas = sum(int(m["hora_fin"]) - int(m["hora_inicio"]) for m in datos)
        horas_por_dia = {}
        for m in datos:
            dia = m["dia"].capitalize()
            duracion = int(m["hora_fin"]) - int(m["hora_inicio"])
            horas_por_dia[dia] = horas_por_dia.get(dia, 0) + duracion
        dia_mas_cargado = max(horas_por_dia, key=horas_por_dia.get) if horas_por_dia else "N/A"
        reporte = {
            "Titulo": "Reporte de Carga Académica y Horario",
            "Resumen_Estadistico": {
                "Total_Materias_Diferentes": total_materias_unicas,
                "Total_Sesiones_Semanales": total_sesiones,
                "Total_Horas_Semanales": total_horas,
                "Dia_Con_Mas_Horas": dia_mas_cargado
            },
            "Lista_Materias_Unicas": materias_unicas,
            "Detalle_Horarios": [
                {
                    "materia": m["materia"],
                    "dia": m["dia"],
                    "hora_inicio": f"{m['hora_inicio']}:00",
                    "hora_fin": f"{m['hora_fin']}:00",
                    "ubicacion": m["ubicacion"]
                }
                for m in datos
            ]
        }

        with open("reporte.json", "w", encoding="utf-8") as archivo_reporte:
            json.dump(reporte, archivo_reporte, indent=4, ensure_ascii=False)
        print("\n" + "=" * 50)
        print("         REPORTE GENERAL DE HORARIO")
        print("=" * 50)
        print(f"• Total de materias únicas: {total_materias_unicas}")
        print(f"• Total de sesiones semanales: {total_sesiones}")
        print(f"• Total de horas de clase a la semana: {total_horas} hrs")
        print(f"• Día con mayor carga lectiva: {dia_mas_cargado}")
        print("-" * 50)
        print("DETALLE DE HORARIOS:")        
        for i, m in enumerate(datos, start=1):
            print(f"{i}. {m['materia']} | {m['dia']} | {m['hora_inicio']}:00 - {m['hora_fin']}:00 | {m['ubicacion']}")            
        print("=" * 50)
        print("¡Reporte generado exitosamente en 'reporte.json'!\n")
    except FileNotFoundError:
        print("\nNo se encontró el archivo 'Datos.json'. Asegúrese de registrar materias primero.")
    except json.JSONDecodeError:
        print("\nEl archivo 'Datos.json' está vacío o tiene un formato no válido.")