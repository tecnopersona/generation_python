class Pelota():
    #atributo
    forma= "cuadrada"
    
    #metodo constructor
    #def __init__(self):
    #    self.color = None
    #    self.tamaño = 15
    #    self.material = "plástico"
    ###
    #metodo constructor con parametros    
    def __init__(self, color: str, tamaño: int):
        self.color = color
        self.tamaño = tamaño
        #self.material = material
    
    #2 tipos de metodos (estaticos y no estaticos o de instancia)
    #@staticmethod es un decorador
    @staticmethod
    def crear_rebotes():
        return [5,4,3,2,1,0]
    
    def asignar_color(self):
        self.color = "naranja"
        
    def asignar_color2(self,color):
        self.color = color
        
    #accesador y mutador
    @property#permite acceder al atributo como si fuera un atributo normal
    def color_material(self):
        return f"{self.color} - {self.material}"
        
    @property# getter
    def material(self):
        return self.material
    
    @material.setter# setter o mutador
    def material(self,tipo_material: str):
        self.material = tipo_material
    