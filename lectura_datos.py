import csv  # Módulo para leer archivos CSV

def cargar_datos(ruta_archivo):
    base_datos = []  # Lista donde se guardarán todos los registros

    try:
        # Lectura del archivo CSV
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            # Recorre cada fila y la convierte en diccionario
            for fila in lector:
                persona = {
                    "id": int(fila["id"]),
                    "nombre": fila["nombre"],
                    "edad": int(fila["edad"]),
                    "ciudad": fila["ciudad"],

                    # Diccionario anidado académico
                    "datos_academicos": {
                        "carrera": fila["carrera"],
                        "semestre": int(fila["semestre"]),
                        "promedio": float(fila["promedio"])
                    },

                    # Diccionario anidado laboral
                    "datos_laborales": {
                        "trabaja": fila["trabaja"] == "True",
                        "ingreso_mensual": float(fila["ingreso_mensual"])
                    },

                    # Diccionario anidado tecnológico
                    "datos_tecnologicos": {
                        "internet": fila["internet"] == "True",
                        "computadora": fila["computadora"] == "True"
                    }
                }

                # Guardar cada persona en la lista
                base_datos.append(persona)

    # Manejo de errores
    except FileNotFoundError:
        print("Error: No se encontró el archivo")
    except ValueError as e:
        print("Error en conversión de datos:", e)

    # Retornar todos los datos cargados
    return base_datos