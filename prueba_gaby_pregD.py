from Personaje import Personaje
from ApiPeopleDev import cargar_api
import requests

class Personaje:
    personajes_obj = []
    def __init__(self, nombre, planeta_origen, episodios, genero, especie, naves, vehiculos):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        self.episodios = episodios
        self.genero = genero
        self.especie = especie
        self.naves = naves
        self.vehiculos = vehiculos

def buscar_personaje(nombre):
    url = "https://swapi.dev/api/people/"
    response = requests.get(url, params={"search": nombre})
    return response.json()["results"]

def obtener_info_personaje(personaje):
    nombre = personaje["name"]
    url_planeta = personaje["homeworld"]
    planeta=cargar_api(url_planeta)
    nombre_planeta = planeta["name"]

    urls_peliculas = personaje["films"]
    episodios = []
    for url_pelicula in urls_peliculas:
        datos_pelicula = cargar_api(url_pelicula)
        episodios.append(datos_pelicula["episode_id"])

    urls_especies = personaje["species"]
    especie = ""
    
    if not urls_especies:
        url_especie = cargar_api("https://swapi.dev/api/species/")
        datos_especie = url_especie  
        while True:
            for info_especie in datos_especie["results"]:
                if info_especie["name"] == "Unknown":
                    especie = info_especie["name"]
                    break
            if especie or not datos_especie["next"]:
                break
            datos_especie = cargar_api(datos_especie["next"])
    else:
        respuesta_especie = requests.get(urls_especies[0])
        datos_especie = respuesta_especie.json()
        especie = datos_especie["name"]

    urls_naves = personaje["starships"]
    naves = []
    for url_nave in urls_naves:
        datos_nave = cargar_api(url_nave)
        naves.append(datos_nave["name"])

    urls_vehiculos = personaje["vehicles"]
    vehiculos = []
    if not urls_vehiculos:
        datos_vehiculo = cargar_api("https://swapi.dev/api/vehicles/")
        while True:
            for info_vehiculo in datos_vehiculo["results"]:
                vehiculos.append(info_vehiculo["name"])
            if not datos_vehiculo["next"]:
                break
            url_vehiculo = datos_vehiculo["next"]
    else:
        for url_vehiculo in urls_vehiculos:
            respuesta_vehiculo = requests.get(url_vehiculo)
            datos_vehiculo = respuesta_vehiculo.json()
            vehiculos.append(datos_vehiculo["name"])

    return {
        "nombre": nombre,
        "planeta_origen": nombre_planeta,
        "peliculas": episodios,
        "especie": especie,
        "naves": naves,
        "vehiculos": vehiculos,
        "genero": personaje["gender"]
    }

def buscando_personaje():
    nombre = input("Ingrese el nombre de un personaje: ")
    personajes = buscar_personaje(nombre)
    for personaje in personajes:
        info = obtener_info_personaje(personaje)
        personaje_obj = Personaje(
            nombre=info["nombre"],
            planeta_origen=info["planeta_origen"],
            episodios=info["peliculas"],
            genero=info["genero"],
            especie=info["especie"],
            naves=info["naves"],
            vehiculos=info["vehiculos"]
        )
        Personaje.personajes_obj.append(personaje_obj)
        print("Nombre:", personaje_obj.nombre)
        print("Planeta de origen:", personaje_obj.planeta_origen)
        print("Episodios en los que interviene:", ", ".join([str(episodio) for episodio in personaje_obj.episodios]))
        print("Especie:", personaje_obj.especie)
        print("Naves:", ", ".join(personaje_obj.naves))
        print("Vehiculos:", ", ".join(personaje_obj.vehiculos))
        print("Genero:", personaje_obj.genero)
        print()

buscando_personaje()