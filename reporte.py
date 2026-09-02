import json
def generar_reporte():
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        if not datos:
            print("No hay materias registradas para generar un reporte.")
            return
        materias_unicas = set(m["materia"].capitalize() for m in datos)
        reporte = {
            "Titulo": "Reporte de Materias Registradas",
            "Total de Materias": len(materias_unicas),
            "Materias": list(materias_unicas),
            "Dias y Horarios": [
                {
                    "materia": m["materia"],
                    "dia": m["dia"],
                    "hora_inicio": m["hora_inicio"],
                    "hora_fin": m["hora_fin"],
                    "ubicacion": m["ubicacion"]
                } for m in datos
            ]
        }
        with open("reporte.json", "w", encoding="utf-8") as archivo_reporte:
            json.dump(reporte, archivo_reporte, indent=4, ensure_ascii=False)
        print("Reporte generado exitosamente en 'reporte.json'.")
        total_materias = len(materias_unicas)
        print(f"Total de materias registradas: {total_materias}")
        for i, m in enumerate(datos, start=1):
            print(f"{i}. Materia: {m['materia']}, Día: {m['dia']}, Hora: {m['hora_inicio']} - {m['hora_fin']}, Ubicación: {m['ubicacion']}")
    except FileNotFoundError:
        print("No se encontró el archivo de datos. Asegúrese de registrar materias primero.")
