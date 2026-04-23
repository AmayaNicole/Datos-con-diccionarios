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

# Reporte 7: Cantidad de personas con internet
print("\n7. Cantidad de personas con internet:")
print(personas_con_internet(datos))

# Reporte 8: Cantidad de personas con computadora
print("\n8. Cantidad de personas con computadora:")
print(personas_con_computadora(datos))

# Reporte 9: Promedio académico de personas que trabajan
print("\n9. Promedio académico de personas que trabajan:")
print(promedio_personas_que_trabajan(datos))

# Reporte 10: promedio academico de personas que no tarabajan
print("\n10. promedio academico de personas que no tarabajan:")
print(promedio_personas_que_no_trabajan(datos)) # Fin de los segundos 5 bloques correspondientes a los reportes 6-10

# ========================= Imprimiendo reportes 16 - 20 ================================
print("\n" + "="*70)
print("REPORTES 16-20".center(70,"-"))
print("="*70)

print("\n16. Relación entre ingreso y promedio académico:")
print(relacion_ingreso_promedio(datos))

print("\n17. Cantidad de personas por rango de edad:")
print(personas_por_rango_edad(datos))

print("\n18. Promedio académico por ciudad:")
print(promedio_por_ciudad(datos))

print("\n19. Porcentaje de personas que trabajan:")
print(porcentaje_personas_que_trabajan(datos))

print("\n20. Perfil promedio del encuestado:")
perfil = perfil_promedio(datos)
for clave, valor in perfil.items():
    print(f"    - {clave}: {valor}")