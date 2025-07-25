print("Hola Mundo!!")
print('Hola 2 mundos')

# variables, estan definidas por el contenido
nombre= "Israel"
print(nombre)
#nombre = 2
print(nombre)

#nombre de la variable debe ser significativo
uno_caracter = "1"
uno_palabra = "uno"
uno_numero = 1

#interpolacion de cadenas

print("Hola "+ nombre)# Hola Israel
print("hola",nombre)
edad = 45
print(f"mi nombre es {nombre}, tengo {edad} años")

# %
print("mi nombre es %s, tengo %d años" % (nombre, edad))

print(len(nombre)) # longitud de la cadena