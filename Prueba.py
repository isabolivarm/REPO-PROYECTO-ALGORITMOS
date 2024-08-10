from ApiVehicles import cargar_api
from ApiStarships import cargar_api
#from ApiSpecies import cargar_especies
#from ApiPlanets import cargar_planetas
from ApiPeople import cargar_api
from ApiFilms import cargar_api
from Film import Film
from Weapon import Weapon
from Starship import Starship
import csv
#import matplotlib.pyplot as plt
#import tabulate
import statistics
from Mision import Mision
import requests
from Personaje import Personaje

class Prueba:
  
    def start(self):
        self.buscando_personaje()

    def buscar_personaje(self,nombre):
        url = "https://swapi.dev/api/people/"
        response = requests.get(url, params={"search": nombre})
        return response.json()["results"]

    def obtener_info_personaje(self,personaje):
        nombre = personaje["name"]
        url_planeta = personaje["homeworld"]
        planeta=cargar_api(url_planeta)
        nombre_planeta = planeta["name"]

        urls_peliculas = personaje["films"]
        episodios = []
        for url_pelicula in urls_peliculas:
            datos_pelicula = cargar_api(url_pelicula)
            episodios.append(datos_pelicula["episode_id"])

        species_urls = personaje["species"]
        especie = ""
        if not species_urls:
            species_url = "https://swapi.dev/api/species/"
            while True:
                species_response = requests.get(species_url)
                species_data = species_response.json()
                for species_info in species_data["results"]:
                    if species_info["name"] != "Unknown":
                        especie = species_info["name"]
                        break
                if especie or not species_data["next"]:
                    break
                species_url = species_data["next"]
        else:
            species_response = requests.get(species_urls[0])
            species_data = species_response.json()
            especie = species_data["name"]

        
        urls_naves = personaje["starships"]
        naves = []
        if not urls_naves:
            buscar_naves=cargar_api("https://swapi.dev/api/starships/")
            for nave in buscar_naves["results"]:
                for piloto in nave["pilots"]:
                    if piloto==personaje["url"]:
                       naves.append(nave["name"])
        else:
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
                    print(info_vehiculo) 
                if not datos_vehiculo["next"]:
                    break
                url_vehiculo = datos_vehiculo["next"]
        else:
            for url_vehiculo in urls_vehiculos:
                respuesta_vehiculo = requests.get(url_vehiculo)
                datos_vehiculo = respuesta_vehiculo.json()
                if "name" in datos_vehiculo:
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

    def buscando_personaje(self):
        nombre = input("Ingrese el nombre de un personaje: ")
        personajes = self.buscar_personaje(nombre)
        for personaje in personajes:
            info = self.obtener_info_personaje(personaje)
            personaje_obj = Personaje(
                nombre=info["nombre"],
                planeta_origen=info["planeta_origen"],
                episodios=info["peliculas"],
                genero=info["genero"],
                especie=info["especie"],
                naves=info["naves"],
                vehiculos=info["vehiculos"]
            )
            self.personajes_obj.append(personaje_obj)
            print("Nombre:", personaje_obj.nombre)
            print("Planeta de origen:", personaje_obj.planeta_origen)
            print("Episodios en los que interviene:", ", ".join([str(episodio) for episodio in personaje_obj.episodios]))
            print("Especie:", personaje_obj.especie)
            print("Naves:", ", ".join(personaje_obj.naves))
            print("Vehiculos:", ", ".join(personaje_obj.vehiculos))
            print("Genero:", personaje_obj.genero)
            print()