from lectura_datos import *  # Importa la funcion para leer y estructurar los datos desde el CSV
from reportes import * #Importa el archivo con la logica de los reportes

# Ruta del archivo
ruta = "dataset_10000_personas.csv"

# Llamar la función
datos = cargar_datos(ruta)

# Mostrar resultados
print("Total de registros:", len(datos))

# Recorre y muestra solo la primera persona como ejemplo
for persona in datos[:1]:
    print(persona)

# ========================= Imprimiendo reportes 1 - 5  ================================
print("\n" + "="*70)
print("REPORTES 1-5".center(70,"-"))
print("="*70)

#Imprime el resultado obtenido de cada iteracion
print("1. Personas por ciudad:")
print(personas_por_ciudad(datos))

print("\n2. Personas por carrera:")
print(personas_por_carrera(datos))

print("\n3. Promedio general:")
print(promedio_general(datos))

print("\n4. Promedio por carrera:")
print(promedio_por_carrera(datos))

print("\n5. Personas que trabajan:")
print(personas_que_trabajan(datos)) #Fin de los primeros 5 bloques correspondientes a los primeros 5 reportes

# ========================= Imprimiendo reportes 6 - 10 ================================
print("\n" + "="*70)
print("REPORTES 6-10".center(70,"-"))
print("="*70)
# Reporte 6: Promedio de ingresos
print("\n6. Promedio de ingresos:")
print(promedio_ingresos(datos))
