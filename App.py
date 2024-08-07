from ApiVehicles import cargar_api
from ApiStarships import cargar_api
from ApiSpecies import cargar_especies
from ApiPlanets import cargar_planetas
from ApiPeople import cargar_api
from ApiFilms import cargar_api
from Film import Film
import csv
from Weapons import Weapon

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


    def transformar_weapons(self): #TENGO QUE REVISAR ESTO
        for weapon_name in self.lista_csv_weapons:
            self.weapons_obj.append(Weapon(weapon_name))



    def crear_mision(self):
        i=0
        while i<5:
            print("Creemos una nueva misión")

            while True:
                nombre_mision=input("Ingrese el nombre de la mision: ")
                planeta_destino = input("Ingrese el planeta destino: ")
                while  planeta_destino not in self.planets_obj:
                    print("Planeta inválido. Intente nuevamente")
                    planeta_destino = input("Ingrese el planeta destino: ")
                
                nave_utilizar = input("Ingrese la nave a utilizar: ")  
                while nave_utilizar not in self.spaceships_obj:
                    print("Nave inválida. Intente nuevamente.")
                    nave_utilizar = input("Ingrese la nave a utilizar: ")

                armas_utilizar = []
                n = 0

                while n < 7:
                    arma_seleccionada = input("Ingrese una arma o 0 para finalizar: ")


                    if arma_seleccionada==0:
                        break
                    elif arma_seleccionada in self.weapons_obj:
                        armas_utilizar.append(arma_seleccionada)
                        n += 1
                    else:
                        print("Arma inválida. Intente nuevamente.")

                integrantes_mision=[]
                m=0

                while m<7:
                    integrante_seleccionado= input("Ingrese un integrante de la misión o 0 para finalizar: ")
                    if integrante_seleccionado==0:
                        break
                    elif integrante_seleccionado in self.characters_obj:
                        integrantes_mision.append(integrante_seleccionado)
                        m+=1
                    else:
                        print("Integrante inválido. Intente nuevamente")
                        
        print('Mision creada con exito')
        
        i+=1



    




    
    def menu():
        print("Ingrese el número de opción que desea explorar")
        print("1. Explorar las películas de la saga")
        print("2. Explorar las especies de seres vivos")
        print("3. Buscar un personaje")
        print("4. Crear un gráfico de personajes según su planeta de nacimiento")
        print("5. Crear un gráfico para comparar las naves")
        print("6. Conocer las estadísticas de las naves")
        print("7. Crear una misión")
        opcion_menu=int(input("-->"))

    



