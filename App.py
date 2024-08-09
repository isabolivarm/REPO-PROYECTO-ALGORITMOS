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
import tabulate
import statistics
from Mision import Mision

class App:
    film_obj=[]
    planets_obj=[]
    characters_obj=[]
    spaceships_obj=[]
    weapons_obj=[]
    species_obj=[]
    vehicles_obj=[]
    misiones_obj=[]
    
    def start(self):
        print("hola")
        self.crear_films()
        self.cargar_starships()
        
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
                dict_characters = self.abrir_characters()
                self.graficos_personajes_planetas(dict_characters)
            
            elif opcion_menu=="6":
               self.estadisticas_naves()

            elif opcion_menu=="7":
                print("cambiar esto")

            elif opcion_menu=="8":
                break
        

    def crear_films(self):
        self.film_obj = []  
        dbfilms = cargar_api("https://www.swapi.tech/api/films/")
        for film in dbfilms["result"]:
            self.film_obj.append(Film(  
                title=film["properties"]["title"],
                episode_id=film["properties"]["episode_id"],
                release_date=film["properties"]["release_date"],
                opening_crawl=film["properties"]["opening_crawl"],
                director=film["properties"]["director"]))

    def print_films(self):
        for film in self.film_obj:
            print(f"Titulo: {film.title}")
            print(f"Numero de episodio: {film.episode_id}")
            print(f"Fecha de lanzamiento: {film.release_date}")
            print(f"Opening Crawl: {film.opening_crawl}")
            print(f"Director: {film.director}")
            print("---")

    def cargar_starships(self):
        self.starships_obj = []
        with open("starships.csv", "r") as archivo_starships:
            reader = csv.reader(archivo_starships)
            next(reader)
            for row in reader:
                nombre = row[1]
                if row[11] == '':
                    hiperimpulsor = 0.0
                else:
                    hiperimpulsor = float(row[11])

                if row[12] == '':
                    mglt = 0.0
                else:
                    mglt = float(row[12])

                if row[6] == '':
                    velocidad_max_atm = 0.0
                else:
                    velocidad_max_atm = float(row[6])

                if row[4] == '':
                    costo_creditos = 0.0
                else:
                    costo_creditos = float(row[4])
                self.starships_obj.append(Starship(nombre, hiperimpulsor, mglt, velocidad_max_atm, costo_creditos))


    def estadisticas_naves(self):
        hiper_impulsores = []
        mglt = []
        velocidad_maxima = []
        costo_credito = []
        for starship in self.starships_obj:
            hiper_impulsores.append(starship.hiperimpulsor)
            mglt.append(starship.mglt)
            velocidad_maxima.append(starship.velocidad_max_atm)
            costo_credito.append(starship.costo_creditos)

        estadisticas_starships = {
            "Hiperimpulsor": {
                "Promedio": statistics.mean(hiper_impulsores),
                "Moda": statistics.mode(hiper_impulsores),
                "Máximo": max(hiper_impulsores),
                "Mínimo": min(hiper_impulsores)
            },
            "MGLT": {
                "Promedio": statistics.mean(mglt),
                "Moda": statistics.mode(mglt),
                "Máximo": max(mglt),
                "Mínimo": min(mglt)
            },
            "Velocidad máxima en la atmósfera": {
                "Promedio": statistics.mean(velocidad_maxima),
                "Moda": statistics.mode(velocidad_maxima),
                "Máximo": max(velocidad_maxima),
                "Mínimo": min(velocidad_maxima)
            },
            "Costo en créditos": {
                "Promedio": statistics.mean(costo_credito),
                "Moda": statistics.mode(costo_credito),
                "Máximo": max(costo_credito),
                "Mínimo": min(costo_credito)
            }
        }

        filas = []
        estadisticas_nombres = ["Promedio", "Moda", "Máximo", "Mínimo"]
        for nombre, stats in estadisticas_starships.items():
            fila = [nombre]
            for stat in estadisticas_nombres:
                fila.append(stats[stat])
            filas.append(fila)

        headers = ["Estadística", "Promedio", "Moda", "Máximo", "Mínimo"]
        print(tabulate.tabulate(filas, headers=headers, tablefmt="grid"))

  


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
            
         
                
                    mision = Mision(nombre_mision, planeta_destino, nave_utilizar, armas_utilizar, integrantes_mision)
                    self.misiones_obj.append(mision)
                
                        
        print('Mision creada con exito')
        
        i+=1

    def ver_mision(self):
        if not self.misiones_obj:
            print("Aun no se han creado misiones")
            return
        print("Misiones:")
        for i, mision in enumerate(f"{self.misiones_obj}"):
            print(f"{i+1}.- {mision["nombre"]}")
            
        seleccionar_mision=int(input("Seleccione una mision para ver sus detalles"))
        mision_seleccionada=self.misiones_obj[seleccionar_mision-1]
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

    
        

    



