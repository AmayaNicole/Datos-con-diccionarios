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