import json
def eliminar_materia():
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo:
            Horario = json.load(archivo)  
        if not Horario:
            print("El horario está vacío.")
            return
        while True: # Solicitar el nombre de la materia a eliminar y validar que no esté vacío
            materia_a_eliminar = input("Ingrese el nombre de la materia que desea eliminar: ").strip()
            if materia_a_eliminar:
                break
            print("Error: El nombre de la materia no puede estar vacío.")
        materias_duplicadas = [evento for evento in Horario if evento["materia"].capitalize() == materia_a_eliminar.capitalize()] # Buscar todas las coincidencias, no solo la primera
        if not materias_duplicadas:
            print(f"No se encontró la materia '{materia_a_eliminar}' en el horario.")
            return
        print(f"Se encontraron {len(materias_duplicadas)} registro(s) de la materia '{materia_a_eliminar}':")
        for evento in materias_duplicadas:
            print(f"- {evento['materia']} el {evento['dia']} de {evento['hora_inicio']}:00 a {evento['hora_fin']}:00 en {evento['ubicacion']}")
        while True:
            confirmacion = input("¿Está seguro de que desea eliminar esta materia? (s/n): ").strip().lower()
            if confirmacion in ['s', 'n']:
                break
            print("Error: Ingrese 's' para sí o 'n' para no.")
        if confirmacion == 'n':
            print("Operación cancelada. No se eliminará la materia.")
            return
        horario_nuevo = [
            evento for evento in Horario 
            if evento["materia"].capitalize() != materia_a_eliminar.capitalize()
        ] # Crear un nuevo horario sin la materia a eliminar 
        
        if len(horario_nuevo) < len(Horario): # Verificar si se eliminó al menos un registro
            with open("Datos.json", "w", encoding="utf-8") as archivo: # Guardar el horario actualizado en el archivo JSON
                json.dump(horario_nuevo, archivo, indent=4, ensure_ascii=False)
            print(f"La materia '{materia_a_eliminar}' ha sido eliminada exitosamente.")
        else:
            print(f"No se encontró la materia '{materia_a_eliminar}' en el horario.")

    except FileNotFoundError:
        print("No se encontró el archivo de datos. Asegúrese de registrar materias primero.")
        return