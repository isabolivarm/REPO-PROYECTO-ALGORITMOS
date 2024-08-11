
class Planeta:
    def __init__(self, id, nombre, orbita, rotacion, poblacion, clima, episodios, personajes):
        self.id = id
        self.nombre = nombre
        self.orbita = orbita
        self.rotacion = rotacion
        self.poblacion = poblacion        
        self.clima = clima
        self.episodios = episodios
        self.personajes = personajes
        
    def imprimir_planeta(self):
        txt_ep = ""
        txt_persons = ""

        for episodio in self.episodios:
            txt_ep += f" {episodio},"
        for personaje in self.personajes:
            txt_persons += f" {personaje},"

        if txt_ep == "":
            txt_ep = " No hay episodios"    
        if txt_persons == "":
            txt_persons = " No hay personajes"
        
        print(f"""
        ID: {self.id}
        Nombre: {self.nombre}
        Periodo de orbita: {self.orbita}  
        Periodo de rotacion: {self.rotacion}              
        Poblacion: {self.poblacion}
        Clima: {self.clima}
        Episodios:{txt_ep}
        Personajes:{txt_persons}""")
