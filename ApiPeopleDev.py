import requests as rq

def cargar_api(link):
    informacion=rq.get(link).json()
    return informacion

cargar_api("https://swapi.dev/api/people")