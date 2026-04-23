from lectura_datos import cargar_datos  # Importa la función
from reportes import * #Importa el archivo con la logica de los reportes

# Ruta del archivo
ruta = "dataset_10000_personas.csv"

# Llamar la función
datos = cargar_datos(ruta)

# Mostrar resultados
print("Total de registros:", len(datos))

# Recorre y muestra solo las primeras 2 personas como ejemplo
for persona in datos[:2]:
    print(persona)


print("\n" + "="*70)
print("REPORTES 1-5".center(70,"-"))
print("="*70)

#Imprime el resultado obtenido de cada iteracion
print("Personas por ciudad:")
print(personas_por_ciudad(datos))

print("\nPersonas por carrera:")
print(personas_por_carrera(datos))

print("\nPromedio general:")
print(promedio_general(datos))

print("\nPromedio por carrera:")
print(promedio_por_carrera(datos))

print("\nPersonas que trabajan:")
print(personas_que_trabajan(datos)) #Fin de los primeros 5 bloques correspondientes a los primeros 5 reportes