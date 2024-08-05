import requests as rq
from Especie import Especie
from Planeta import Planeta

class API:

    # metodo para consultar a la API
    def cargar_api(self, link):
        response = rq.get(link)        
        return response.json()

    # metodo para cargar los personajes
    def cargar_personajes(self):
        personajes = self.cargar_api('https://www.swapi.tech/api/people')
        return personajes

    def cargar_especies(self):
        link = 'https://www.swapi.tech/api/species' 
        lista_especies = []       

        while link:
            # cargar las especies
            especies = self.cargar_api(link)
            # link para la siguiente pagina
            link = especies['next']            

            especies = especies['results']  

            # recorrer las especies
            for especie in especies:
                link_detalle = especie['url']
                detalle_especie = self.cargar_api(link_detalle)
                
                id = detalle_especie['result']['uid']
                detalle_especie = detalle_especie['result']['properties']

                # obtener el nombre del planeta
                planeta = self.cargar_api(detalle_especie['homeworld'])['result']['properties']['name']

                # obtener nombre de los personajes
                personajes = []
                for personaje in detalle_especie['people']:
                    nombre = self.cargar_api(personaje)
                    nombre = nombre['result']['properties']['name']
                    personajes.append(nombre)
                                
                # crear un objeto de la clase Especie
                obj = Especie(id, detalle_especie['name'], detalle_especie['average_height'], detalle_especie['classification'], planeta, detalle_especie['language'], personajes)                
                lista_especies.append(obj)                                           
                              
        return lista_especies

    def cargar_planetas(self):
        link = 'https://www.swapi.tech/api/planets' 
        lista_planetas = []       

        while link:
            # cargar los planetas
            response = self.cargar_api(link)
            # link para la siguiente pagina
            link = response['next']            

            response = response['results']  

            # recorrer los planetas
            for planeta in response:
                link_detalle = planeta['url']
                detalle_planeta = self.cargar_api(link_detalle)

                id = detalle_planeta['result']['uid']
                detalle_planeta = detalle_planeta['result']['properties']                
                                
                # crear un objeto de la clase Planeta
                obj = Planeta(id, detalle_planeta['name'], detalle_planeta['orbital_period'], detalle_planeta['rotation_period'], detalle_planeta['population'], detalle_planeta['climate'])
                lista_planetas.append(obj)                           
                              
        return lista_planetas
        
