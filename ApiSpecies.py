import requests as rq
from Especie import Especie

def cargar_api(link):
    try:
        informacion=rq.get(link).json()
        return informacion
    except:
        print("Error al cargar la API")        

def cargar_especies():
    link = 'https://www.swapi.tech/api/species' 
    lista_especies = []       

    while link:
        # cargar las especies
        especies = cargar_api(link)
        # link para la siguiente pagina
        link = especies['next']            

        especies = especies['results']  

        # recorrer las especies
        for especie in especies:
            link_detalle = especie['url']
            detalle_especie = cargar_api(link_detalle)
            
            id = detalle_especie['result']['uid']
            detalle_especie = detalle_especie['result']['properties']

            # obtener el nombre del planeta
            planeta = cargar_api(detalle_especie['homeworld'])['result']['properties']['name']

            # obtener nombre de los personajes
            personajes = []
            for link_personaje in detalle_especie['people']:
                personaje = cargar_api(link_personaje)
                nombre = personaje['result']['properties']['name']
                personajes.append(nombre)
                            
            # crear un objeto de la clase Especie
            obj = Especie(id, detalle_especie['name'], detalle_especie['average_height'], detalle_especie['classification'], planeta, detalle_especie['language'], personajes)                        
            lista_especies.append(obj)                                           
                            
    return lista_especies

