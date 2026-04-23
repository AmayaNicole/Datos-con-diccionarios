#Reporte 1: Cantidad de personas por ciudad

def personas_por_ciudad(personas): #Definimos la funcion para recibir los datos de personas
    conteo = {} #Creamos un diccionario vacio para guardar resultados

    for p in personas:  #Recorremos cada persona de la lista
        ciudad = p["ciudad"] 

        if ciudad in conteo:  
            conteo[ciudad] += 1  
        else:
            conteo[ciudad] = 1 

    return conteo 


#Reporte 2: Cantidad de personas por carrera

def personas_por_carrera(personas):
    conteo = {}

    for p in personas:
        carrera = p["datos_academicos"]["carrera"]

        if carrera in conteo:
            conteo[carrera] += 1
        else:
            conteo[carrera] = 1

    return conteo


#Reporte 3: Promedio general academico

def promedio_general(personas): 
    suma = 0  

    for p in personas:
        suma += p["datos_academicos"]["promedio"] 

    promedio = suma / len(personas)  #sumamos todos los promedios  y dividimos entre la cantidad total de personas

    return round(promedio, 2) #devolvemos el promedio redondeado a dos decimales para que sean mas claros


#Reporte 4: Promedio por carrera

def promedio_por_carrera(personas):
    suma = {}  
    conteo = {}  

    for p in personas:
        carrera = p["datos_academicos"]["carrera"]  
        promedio = p["datos_academicos"]["promedio"] 

        if carrera in suma:  
            suma[carrera] += promedio  
            conteo[carrera] += 1 
        else:
            suma[carrera] = promedio 
            conteo[carrera] = 1  

    promedios = {} #un nuevo diccionario para los resulados finales

    for carrera in suma:  #ahora recorremos cada carrera acumulada
        promedios[carrera] = round(suma[carrera] / conteo[carrera], 2) #Suma total entre la cantidad y lo redondeamos a dos decimales

    return promedios


#Reporte 5: Cantidad de personas que trabajan

def personas_que_trabajan(personas):
    contador = 0

    for p in personas:
        if p["datos_laborales"]["trabaja"]:
            contador += 1

    return contador

#Reporte 6: Promedio de ingresos

def promedio_ingresos(personas):
    suma = 0 #Almacena la suma total de ingresos
    contador = 0 #Contador para saber cuantas personas trabajan y asi calcular el promedio correctamente

    #Recorremos cada persona para verificar si trabaja y acumular su ingreso
    for p in personas:
        #validamos que el diccionario laboral exista y que la persona trabaje para evitar errores
        if "datos_laborales" in p:
            if p["datos_laborales"]["trabaja"]:
                suma += p["datos_laborales"]["ingreso_mensual"]
                contador += 1

    # Validación para evitar división entre 0
    if contador == 0:
        return 0
    # calculamos promedio
    promedio = round(suma / contador, 2) # round para redondear el resultado a dos decimales
    return promedio

# Reporte 7: Cantidad de personas con internet
def personas_con_internet(personas):
    con_internet = [] #Almacena las personas que tienen internet

    for p in personas:
        # forma corta de validar que el diccionario exista y que la persona tenga computadora
        if "datos_tecnologicos" in p and p["datos_tecnologicos"]["internet"]:
            con_internet.append(p)
    cantidad_personas_con_internet = len(con_internet) #len() para obtener la cantidad de personas con internet

    return cantidad_personas_con_internet

# Reporte 8: Cantidad de personas con computadora
def personas_con_computadora(personas):
    con_computadora = []

    for p in personas:
        if "datos_tecnologicos" in p and p["datos_tecnologicos"]["computadora"]: 
            con_computadora.append(p)
    cantidad_personas_con_computadora = len(con_computadora) 

    return cantidad_personas_con_computadora

# Reporte 9: Promedio académico de personas que trabajan
def promedio_personas_que_trabajan(personas):
    suma = 0 # almacena la suma de los promedios académicos de las personas que trabajan
    contador = 0 # contador para saber cuantas personas trabajan y asi calcular el promedio
    for p in personas:
        if(
            "datos_laborales" in p and
            p["datos_laborales"]["trabaja"] and
            "datos_academicos" in p
        ):
            suma += p["datos_academicos"]["promedio"]
            contador += 1

    # Validación para evitar división entre 0   
    if contador == 0:
        return 0
    # calculamos promedio
    promedio = round(suma / contador, 2) # round para redondear el resultado a dos 
    
    return promedio

# Reporte 10: promedio academico de personas que no tarabajan
def promedio_personas_que_no_trabajan(personas):
    suma = 0 # almacena la suma de los promedios académicos de las personas que no trabajan
    contador = 0 # contador para saber cuantas personas no trabajan y asi calcular el promedio
    for p in personas:
        if(
            "datos_laborales" in p and
            not p["datos_laborales"]["trabaja"] and
            "datos_academicos" in p
        ):
            suma += p["datos_academicos"]["promedio"]
            contador += 1

    # Validación para evitar división entre 0   
    if contador == 0:
        return 0
    # calculamos promedio
    promedio = round(suma / contador, 2) # round para redondear el resultado a dos decimales
    
    return promedio

# ==============================================================================
# REPORTES 16 AL 20
# ==============================================================================

# Reporte 16: Relación entre ingreso y promedio
def relacion_ingreso_promedio(personas):
    # Crea diccionarios para sumar promedios y contar personas por rangos de ingresos
    suma_promedios = {"Sin ingresos": 0, "Bajo (<3000)": 0, "Medio (3000-6000)": 0, "Alto (>6000)": 0}
    conteo_rangos = {"Sin ingresos": 0, "Bajo (<3000)": 0, "Medio (3000-6000)": 0, "Alto (>6000)": 0}

    for p in personas:
        # Valida que los diccionarios existan
        if "datos_laborales" in p and "datos_academicos" in p:
            ingreso = p["datos_laborales"]["ingreso_mensual"]
            promedio = p["datos_academicos"]["promedio"]

            # Clasifica a la persona en un rango
            if ingreso == 0:
                rango = "Sin ingresos"
            elif ingreso < 3000:
                rango = "Bajo (<3000)"
            elif ingreso <= 6000:
                rango = "Medio (3000-6000)"
            else:
                rango = "Alto (>6000)"

            # Acumula el promedio y el conteo en su ranGO
            suma_promedios[rango] += promedio
            conteo_rangos[rango] += 1

    relacion = {} 
    # Calcula el promedio académico por cada rango de ingresos usando .items()
    for rango, suma in suma_promedios.items():
        if conteo_rangos[rango] > 0:
            relacion[rango] = round(suma / conteo_rangos[rango], 2)
        else:
            relacion[rango] = 0

    return relacion

# Reporte 17: Cantidad de personas por rango de edad
def personas_por_rango_edad(personas):
    conteo_edades = {"18-25 años": 0, "26-35 años": 0, "36-45 años": 0, "Mayor de 45 años": 0}

    for p in personas:
        edad = p["edad"]

        # Evaluamos y sumamos al contador correspondiente
        if edad <= 25:
            conteo_edades["18-25 años"] += 1
        elif edad <= 35:
            conteo_edades["26-35 años"] += 1
        elif edad <= 45:
            conteo_edades["36-45 años"] += 1
        else:
            conteo_edades["Mayor de 45 años"] += 1

    return conteo_edades

# Reporte 18: Promedio académico por ciudad
def promedio_por_ciudad(personas):
    suma = {}   
    conteo = {} 

    for p in personas:
        ciudad = p["ciudad"]
        
        # Valida que tenga datos académicos
        if "datos_academicos" in p:
            promedio = p["datos_academicos"]["promedio"]

            if ciudad in suma:
                suma[ciudad] += promedio
                conteo[ciudad] += 1
            else:
                suma[ciudad] = promedio
                conteo[ciudad] = 1

    promedios_finales = {}
    
    # Recorrem para calcular el promedio final por ciudad
    for ciudad in suma:
        promedios_finales[ciudad] = round(suma[ciudad] / conteo[ciudad], 2)

    return promedios_finales

# Reporte 19: Porcentaje de personas que trabajan
def porcentaje_personas_que_trabajan(personas):
    trabajan = 0
    total_personas = len(personas)

    if total_personas == 0:
        return "0%"

    for p in personas:
        if "datos_laborales" in p and p["datos_laborales"]["trabaja"]:
            trabajan += 1

    # Calcula el porcentaje
    porcentaje = (trabajan / total_personas) * 100
    
    return f"{round(porcentaje, 2)}%"

# Reporte 20: Perfil promedio del encuestado
def perfil_promedio(personas):
    suma_edad = 0
    suma_promedio = 0
    total_personas = len(personas)

    # Diccionarios para buscar el dato que más se repite
    conteo_ciudades = {}
    conteo_carreras = {}

    for p in personas:
        suma_edad += p["edad"]

        if "datos_academicos" in p:
            suma_promedio += p["datos_academicos"]["promedio"]
            carrera = p["datos_academicos"]["carrera"]
            
            # Cuenta las carreras
            if carrera in conteo_carreras:
                conteo_carreras[carrera] += 1
            else:
                conteo_carreras[carrera] = 1

        ciudad = p["ciudad"]
        
        # Cuenta las ciudades
        if ciudad in conteo_ciudades:
            conteo_ciudades[ciudad] += 1
        else:
            conteo_ciudades[ciudad] = 1

    # 1. Calculamos promedios numéricos
    edad_promedio = round(suma_edad / total_personas) if total_personas > 0 else 0
    promedio_academico = round(suma_promedio / total_personas, 2) if total_personas > 0 else 0

    # 2. Encuentra los valores más frecuentes  usando .items()
    ciudad_mas_frecuente = ""
    max_ciudad = 0
    for ciudad, cantidad in conteo_ciudades.items():
        if cantidad > max_ciudad:
            max_ciudad = cantidad
            ciudad_mas_frecuente = ciudad

    carrera_mas_frecuente = ""
    max_carrera = 0
    for carrera, cantidad in conteo_carreras.items():
        if cantidad > max_carrera:
            max_carrera = cantidad
            carrera_mas_frecuente = carrera

    # Crea un nuevo diccionario ya estructurado con los datos del perfil 
    perfil = {
        "Edad promedio": edad_promedio,
        "Ciudad predominante": ciudad_mas_frecuente,
        "Carrera predominante": carrera_mas_frecuente,
        "Promedio académico general": promedio_academico
    }

    return perfil