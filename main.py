import csv

def cargar_datos(ruta_archivo):
    base_datos = []

    try:
        # Se usa latin-1 para evitar problema de acentos
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                persona = {
                    "id": int(fila["id"]),
                    "nombre": fila["nombre"],
                    "edad": int(fila["edad"]),
                    "ciudad": fila["ciudad"],
                    "carrera": fila["carrera"],
                    "semestre": int(fila["semestre"]),
                    "promedio": float(fila["promedio"]),
                    
                    # Convierte True/False (string) a booleano real
                    "trabaja": fila["trabaja"] == "True",
                    "ingreso_mensual": float(fila["ingreso_mensual"]),
                    "internet": fila["internet"] == "True",
                    "computadora": fila["computadora"] == "True"
                }

                base_datos.append(persona)

    except FileNotFoundError:
        print("Error: No se encontró el archivo")
    except ValueError as e:
        print("Error en conversión de datos:", e)

    return base_datos


# Uso
ruta = "C:/Users/MINEDUCYT/Documents/DATA_ENGINEERING/diccionarios/dataset_10000_personas.csv"
datos = cargar_datos(ruta)

print("Total de registros:", len(datos))

# Ver ejemplo
for persona in datos[:1]:
    print(persona)