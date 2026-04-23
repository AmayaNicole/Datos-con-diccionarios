from lectura_datos import cargar_datos  # Importa la función

# Ruta del archivo
ruta = "dataset_10000_personas.csv"

# Llamar la función
datos = cargar_datos(ruta)

# Mostrar resultados
print("Total de registros:", len(datos))

# Recorre y muestra solo las primeras 2 personas como ejemplo
for persona in datos[:2]:
    print(persona)