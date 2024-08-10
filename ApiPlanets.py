import requests as rq
from Planeta import Planeta

def cargar_api(link):
    try:
        informacion=rq.get(link).json()   
        return informacion
    except:
        print("Error al cargar la API")

def cargar_planetas():
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
                            
            # crear un objeto de la clase Planeta
            obj = Planeta(id, detalle_planeta['name'], detalle_planeta['orbital_period'], detalle_planeta['rotation_period'], detalle_planeta['population'], detalle_planeta['climate'])
            lista_planetas.append(obj)                           
                            
    return lista_planetas
        