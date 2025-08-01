#importar
from pelota import Pelota

#instancia de la clase, o creacion de un objeto
pelota_de_israel = Pelota("Morado",10)
pelota2 = Pelota("Blanco", 18)

print(pelota_de_israel)#<Pelota.Pelota object at 0x0000024BE4FF5DF0>
print(pelota2)#<Pelota.Pelota object at 0x0000024BE4FF5E20>

#accediendo al contenido por default del atributo 
print(pelota_de_israel.forma)
print(pelota2.forma)

pelota_de_israel.forma = "redonda"
print(pelota_de_israel.forma)

#llamando al metodo estatico
print(Pelota.crear_rebotes()) # [5, 4, 3, 2, 1, 0]

#print(pelota2.color)#AttributeError: 'Pelota' object has no attribute 'color'
print(pelota2.asignar_color())
#print(Pelota.asignar_color())#TypeError: Pelota.asignar_color() missing 1 required positional argument: 'self'

print(pelota2.color)
#print(pelota_de_israel.color)#AttributeError: 'Pelota' object has no attribute 'color'


color = input("Ingrese el color de la pelota: ")
pelota_de_israel.asignar_color2(color)
print(pelota_de_israel.color)

pelota3 = Pelota("Blanco",5)
print(pelota3.color, pelota3.tamaño)

#pelota3.asignar_color2("verde")
pelota3.asignar_color()
print(pelota3.color, pelota3.tamaño)

pelota4 =Pelota("Verde",19)
print(pelota4.color, pelota4.tamaño)

#accediendo al accesor y mutador
pelota4.material("metal")


print(pelota4.color_material)  # Verde - metal

print(pelota4.material)#getter


#instalar postgresql clave Admin1234