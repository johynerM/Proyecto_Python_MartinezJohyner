import json
def eliminar_materia():
    try:
        with open("Datos.json", "r", encoding="utf-8") as archivo:
            Horario = json.load(archivo)  
        materia_a_eliminar = input("Ingrese el nombre de la materia que desea eliminar: ")
        horario_nuevo = [
            evento for evento in Horario 
            if evento["materia"].capitalize() != materia_a_eliminar.capitalize()
        ]
        
        if len(horario_nuevo) < len(Horario):
            with open("Datos.json", "w", encoding="utf-8") as archivo:
                json.dump(horario_nuevo, archivo, indent=4, ensure_ascii=False)
            print(f"La materia '{materia_a_eliminar}' ha sido eliminada exitosamente.")
        else:
            print(f"No se encontró la materia '{materia_a_eliminar}' en el horario.")

    except FileNotFoundError:
        print("No se encontró el archivo de datos. Asegúrese de registrar materias primero.")
        return