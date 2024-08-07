
class Planeta:
    def __init__(self, id, nombre, orbita, rotacion, poblacion, clima):
        self.id = id
        self.nombre = nombre
        self.orbita = orbita
        self.rotacion = rotacion
        self.poblacion = poblacion        
        self.clima = clima
        
    def imprimir_planeta(self):
        print(f"""
        ID: {self.id}
        Nombre: {self.nombre}
        Periodo de orbita: {self.orbita}  
        Periodo de rotacion: {self.rotacion}              
        Poblacion: {self.poblacion}
        Clima: {self.clima}""")
