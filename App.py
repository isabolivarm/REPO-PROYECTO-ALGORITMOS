from ApiVehicles import cargar_api
from ApiStarships import cargar_api
from ApiSpecies import cargar_especies
from ApiPlanets import cargar_planetas
from ApiPeople import cargar_api
from ApiFilms import cargar_api
from Film import Film
import csv
file_path="C:\Users\Gaby_\Downloads\starwars.zip\csv"
with open (file_path,"r") as file:
    csv_reader=csv.reader(file)
    header=next(csv_reader)
    data=[row for row in csv_reader]

print("Encabezado:",header)
print("Primeras filas de datos: ",data[:5])
class App:
    film_obj=[]
    planets_obj=[]
    characters_obj=[]
    spaceships_obj=[]
    weapons_obj=[]
    species_obj=[]
    vehicles_obj=[]


    def crear_films(self):
        dbfilms=cargar_api("https://www.swapi.tech/api/films/")
        for film in dbfilms:
            self.film_obj.append(Film(film["title"]),(film["episode_id"]),(film["release_date"]),(film["opening_crawl"]),(film["director"]) )
        
    def print_films(self):
        for film in self.film_obj:
            print(f"Titulo: {film.title}")
            print(f"Numero de episodio: {film.episode_id}")
            print(f"Fecha de lanzamiento: {film.release_date}")
            print(f"Opening Crawl: {film.opening_crawl}")
            print(f"Director: {film.director}")
            print("---")






    def crear_mision(self):
        print("Creemos una nueva misión")
        nombre_mision=input("Ingrese el nombre de la mision: ")
        while True:
            planeta_destino = input("Ingrese el planeta destino: ")
           # if planeta_destino not in #lista de planetas objetos
         #       print("Planeta inválido")
         #   else:
            break


        armas_utilizar = []
        n = 0


        while n < 7:
            arma_seleccionada = input("Ingrese una arma o 0 para finalizar: ")


            if arma_seleccionada==0:
                break
           # elif arma_seleccionada in #lista de armas
           #     armas_utilizar.append(arma_seleccionada)
           #     n += 1
            else:
                print("Arma inválida. Intente nuevamente.")


            integrantes_mision=[]
            m=0


        while n<7:
            integrante_seleccionado= input("Ingrese un integrante de la misión o 0 para finalizar: ")


            if integrante_seleccionado==0:
                break
            #elif integrante_seleccionado in #lista de people
             #   integrantes_mision.append(integrante_seleccionado)
               # m+=1
            else:
                print("Integrante inválido. Intente nuevamente")
