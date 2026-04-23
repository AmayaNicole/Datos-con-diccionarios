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