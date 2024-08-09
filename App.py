from ApiVehicles import cargar_api
from ApiStarships import cargar_api
from ApiSpecies import cargar_especies
from ApiPlanets import cargar_planetas
from ApiPeople import cargar_api
from ApiFilms import cargar_api
from Film import Film
from Weapon import Weapon
from Starship import Starship
import csv
import matplotlib.pyplot as plt

class App:
    film_obj=[]
    planets_obj=[]
    characters_obj=[]
    spaceships_obj=[]
    weapons_obj=[]
    species_obj=[]
    vehicles_obj=[]
    misiones=[]
    
    def start(self):
        print("hola")
        self.crear_films()
        
        print("Bienvenidos a esta aventura")
        while True:
            opcion_menu=input("""Ingrese el número de opción que desea explorar
            1. Explorar las películas de la saga
            2. Explorar las especies de seres vivos
            3. Buscar un personaje
            4. Crear un gráfico de personajes según su planeta de nacimiento
            5. Crear un gráfico para comparar las naves
            6. Conocer las estadísticas de las naves
            7. Crear una misión
            8. Salir
            --> """)

            if opcion_menu =="1":
                 self.print_films()
                
            elif opcion_menu=="2":
                print("hola")
                
            elif opcion_menu=="3":
                print("cambiar esto")
            
            elif opcion_menu=="4":
                print("cambiar esto")
                
            elif opcion_menu=="5":
                print("cambiar esto")
            
            elif opcion_menu=="6":
                print("cambiar esto")

            elif opcion_menu=="7":
                print("cambiar esto")

            elif opcion_menu=="8":
                break
        


  #def crear_films(self):
  #      dbfilms=cargar_api("https://www.swapi.tech/api/films/")
 #       for film in dbfilms:
   #         self.film_obj.append(Film(film["title"]),(film["episode_id"]),(film["release_date"]),(film["opening_crawl"]),(film["director"]) )


    def crear_films(self):
        self.film_obj = []  
        dbfilms = cargar_api("https://www.swapi.tech/api/films/")
        for film in dbfilms:
            self.film_obj.append(Film(**film))

    def print_films(self):
        for film in self.film_obj:
            print(f"Titulo: {film.title}")
            print(f"Numero de episodio: {film.episode_id}")
            print(f"Fecha de lanzamiento: {film.release_date}")
            print(f"Opening Crawl: {film.opening_crawl}")
            print(f"Director: {film.director}")
            print("---")



    def crear_mision(self):
        i=0
        while i<6:
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
            
         
                
                mision = {'nombre': nombre_mision, 'planeta_destino': planeta_destino, 'nave_utilizar': nave_utilizar,'armas_utilizar': armas_utilizar, 'integrantes_mision': integrantes_mision}
                self.misiones.append(mision)
                
                        
        print('Mision creada con exito')
        
        i+=1

    def ver_mision(self):
        if not self.misiones:
            print("Aun no se han creado misiones")
            return
        print("Misiones:")
        for i, mision in enumerate(f"{self.misiones}"):
            print(f"{i+1}.- {mision["nombre"]}")
            
        seleccionar_mision=int(input("Seleccione una mision para ver sus detalles"))
        mision_seleccionada=self.misiones[seleccionar_mision-1]
        print ("Detalles de la mision: ")
        print(f"Nombre: {mision_seleccionada["nombre"]}")
        print(f"Planeta destino: {mision_seleccionada['planeta_destino']}")
        print(f"Nave utilizada: {mision_seleccionada['nave_utilizar']}")

        print("Armas utilizadas:")
        for arma in mision_seleccionada['armas_utilizar']:
            print(f"- {arma}")

        print("Integrantes de la misión:")
        for integrante in mision_seleccionada['integrantes_mision']:
            print(f"- {integrante}")
    
    def transformar_weapons(self): #TENGO QUE REVISAR ESTO
            for weapon_name in self.lista_csv_weapons:
                self.weapons_obj.append(Weapon(weapon_name))



    def abrir_characters():
        with open('characters.csv', 'r') as csv_characters:
            reader = csv.reader(csv_characters)
            data = list(reader) 
        dict_characters = {row[1]: row[10] for row in data[1:]}  
        return dict_characters

    def graficos_personajes_planetas(dict_characters):
        planetas = {}
        for character, planeta in dict_characters.items():
            if planeta in planetas: 
                planetas[planeta] += 1
            else: 
                planetas[planeta] = 1

        plt.bar(planetas.keys(), planetas.values())
        plt.xlabel("Planeta")
        plt.ylabel("Cantidad de personajes")
        plt.title("Cantidad de personajes por planeta")
        plt.xticks(rotation=90)  
        plt.show()

    dict_characters = abrir_characters()
    graficos_personajes_planetas(dict_characters)
        

    



