

class Especie:
    def __init__(self, id, nombre, altura, clasificacion, planeta, lengua, personajes):
        self.id = id
        self.nombre = nombre
        self.altura = altura
        self.clasificacion = clasificacion        
        self.planeta = planeta
        self.lengua = lengua
        self.personajes = personajes
        #self.episodios = episodios
    
    def imprimir_especie(self):
        print(f"""
        ID: {self.id}
        Nombre: {self.nombre}
        Altura promedio: {self.altura}
        Clasificacion: {self.clasificacion}
        Planeta: {self.planeta}
        Lengua: {self.lengua}
        Personajes: {self.personajes}""")
    

    
        



