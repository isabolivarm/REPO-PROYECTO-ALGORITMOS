import requests as rq


def cargar_api(link):
    informacion=rq.get(link).json()
    return informacion

cargar_api("https://www.swapi.tech/api/people/")