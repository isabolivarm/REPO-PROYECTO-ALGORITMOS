import requests as rq
from Planeta import Planeta

def cargar_api(link):
    try:
        informacion=rq.get(link).json()   
        return informacion
    except:
        print("Error al cargar la API")

def cargar_planetas(personajes_obj):
    link = 'https://www.swapi.tech/api/planets' 
    lista_planetas = []       

    while link:
        # cargar los planetas
        response = cargar_api(link)
        # link para la siguiente pagina
        link = response['next']            

        response = response['results']  

        # recorrer los planetas
        for planeta in response:
            link_detalle = planeta['url']
            detalle_planeta = cargar_api(link_detalle)

            id = detalle_planeta['result']['uid']
            detalle_planeta = detalle_planeta['result']['properties']    

            # obtener nombre de los episodios
            episodios = []            
            datos_episodios = cargar_api('https://www.swapi.tech/api/films')
            
            for episodio in datos_episodios['result']:
                if len(episodio['properties']['planets']) > 0:
                    for planeta in episodio['properties']['planets']:
                        if planeta == detalle_planeta['url']:
                            episodios.append(episodio['properties']['title'])              
                            
            # obtener personajes originarios del planeta
            personajes = []
            link_personajes = 'https://www.swapi.tech/api/people'

            if len(personajes_obj) == 0:                
                while link_personajes:
                    response_personajes = cargar_api(link_personajes)
                    link_personajes = response_personajes['next']            

                    response_personajes = response_personajes['results']  

                    for personaje in response_personajes:                    
                        detalle_personaje = cargar_api(personaje['url'])["result"]
                        personajes_obj.append(detalle_personaje)

                        if detalle_personaje['properties']['homeworld'] == detalle_planeta['url']:
                            personajes.append(detalle_personaje['properties']['name'])    
            else:                
                for personaje in personajes_obj:                    
                    if personaje['properties']['homeworld'] == detalle_planeta['url']:
                        personajes.append(personaje['properties']['name'])                            

            # crear un objeto de la clase Planeta
            obj = Planeta(id, detalle_planeta['name'], detalle_planeta['orbital_period'], detalle_planeta['rotation_period'], detalle_planeta['population'], detalle_planeta['climate'], episodios, personajes)
            lista_planetas.append(obj)
            obj.imprimir_planeta()                           
                            
    return lista_planetas
        