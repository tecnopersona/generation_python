#tuplas() , listas[], diccionarios{}
#tupla es inmutable, se ordenan por indice(posicion, comieza en 0)
dias_semana= ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
print(len(dias_semana))#tamaño de la tupla 7
print(dias_semana[len(dias_semana)-1])#acceso al ultimo elemento
#dias_semana[1] = "Jueves" #TypeError: 'tuple' object does not support item assignment


#lista [], se puede modificar, se ordenan por indice(posicion, comieza en 0)
lista_vacia =  []# cero elementos
lista_dia_semana= ["martes", "miércoles", "jueves", "lunes","viernes", "sábado", "domingo"]

lista_vacia[1]="Prueba"


#diccionario{}, son mutables, no tiene orden especifico, se accede por clave
#par ordenado clave:valor
diccionario_vacio = {} # cero elemento
dicc_dias_semana = {
    "lunes": "Monday",
    'numero': 1
    }