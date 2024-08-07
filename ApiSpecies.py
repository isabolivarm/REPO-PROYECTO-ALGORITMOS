import requests as rq


def cargar_api(link):
    informacion=rq.get(link).json()
    print(informacion)
    return informacion

cargar_api("https://www.swapi.tech/api/species/")