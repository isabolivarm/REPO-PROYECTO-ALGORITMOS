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
import requests
from Personaje import Personaje

class App:
    film_obj=[]
    planets_obj=[]
    characters_obj=[]
    spaceships_obj=[]
    weapons_obj=[]
    species_obj=[]
    vehicles_obj=[]
    misiones_obj=[]
    personajes_obj=[]
   
    def start(self):
        self.crear_films()
        self.cargar_starships()
        
        
        print("Bienvenidos a esta aventura")
        while True:
            opcion_menu=input("""Ingrese el número de opción que desea explorar
            1. Explorar las películas de la saga
            2. Explorar las especies de seres vivos
            3. Visualizar planetas
            4. Buscar un personaje
            5. Crear un gráfico de personajes según su planeta de nacimiento
            6. Crear un gráfico para comparar las naves
            7. Conocer las estadísticas de las naves
            8. Crear una misión
            9. Modificar una mision
            10. Visualizar mision
            11. Guardar misiones previamente creadas en archivo de texto
            12. Cargar misiones previamente creadas en memoria                 
            13. Salir
            --> """)

            if opcion_menu =="1":
                 self.print_films()
                
            elif opcion_menu=="2":
                # mostrar las especies
                self.species_obj = cargar_especies()
                
            elif opcion_menu=="3":
                # mostrar los planetas
                self.planets_obj = cargar_planetas()
            
            elif opcion_menu=="4":
                self.buscando_personaje()
                
            elif opcion_menu=="5":
                dict_characters=self.abrir_characters()
                self.graficos_personajes_planetas(dict_characters)
            
            elif opcion_menu=="6":
               #grafico para comparacion de naves
               self.grafico_comp_naves()

            elif opcion_menu=="7":
                self.estadisticas_naves()
                
            elif opcion_menu=="8":
                self.crear_mision()
            
            elif opcion_menu=="9":
                # modificar una mision
                self.modificar_mision()
            
            elif opcion_menu=="10":
                self.ver_mision()
            
            elif opcion_menu=="11":
                self.guardar_misiones()
            
            elif opcion_menu=="12":
                self.cargar_misiones()

            elif opcion_menu=="13":
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
        num_misiones = 0
        print("Creemos una nueva misión")
            
        while True:
            nombre_mision=input("Ingrese el nombre de la mision: ")


            planets = []
            with open('planets.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)  
                for row in reader:
                    planets.append(row[1]) 

                print("Planetas disponibles:")
                for i, planet in enumerate(planets):
                    print(f"{i+1}. {planet}")

                planeta_destino = int(input("Ingrese el número del planeta que desea seleccionar: "))

            starships = []
            with open('starships.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)  
                for row in reader:
                    starships.append(row[1]) 

                print("Naves disponibles:")
                for i, starship in enumerate(starships):
                    print(f"{i+1}. {starship}")

                nave_utilizar = int(input("Ingrese el número de la nave que desea seleccionar: "))


            weapons = []
            with open('weapons.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
                next(reader) 
                for row in reader:
                    weapons.append(row[1])  

            print("Armas disponibles:")
            for i, weapon in enumerate(weapons):
                print(f"{i+1}. {weapon}")

            armas_utilizar = []
            while len(armas_utilizar) < 7:
                arma_seleccionada = int(input("Ingrese el número de la arma que desea seleccionar (o 0 para finalizar): "))
                if arma_seleccionada == 0:
                    break
                armas_utilizar.append(weapons[arma_seleccionada-1])
                print(f"Ha seleccionado: {armas_utilizar[-1]}")

                
            characters = []
            with open('characters.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
                next(reader) 
                for row in reader:
                    characters.append(row[1])  
            print("Personajes disponibles:")
            for i, character in enumerate(characters):
                print(f"{i+1}. {character}")

            integrantes_mision = []
            while len(integrantes_mision) < 7:
                integrante_seleccionado = int(input("Ingrese el número del personaje que desea seleccionar (o 0 para finalizar): "))
                if integrante_seleccionado == 0:
                    break
                integrantes_mision.append(characters[integrante_seleccionado-1])
                print(f"Ha seleccionado: {integrantes_mision[-1]}")
               


         
                
                mision = Mision(nombre_mision, planeta_destino, nave_utilizar, armas_utilizar, integrantes_mision)
                self.misiones_obj.append(mision)
            print('mision creada con exito')
            num_misiones += 1

                
            if num_misiones >= 5:
                print("No puedes crear más misiones")
                break
        
            respuesta = input("¿Desea crear otra misión? (si/no): ")
            if respuesta.lower() == 'no':
                break

    def guardar_misiones(self):
        with open('misiones.txt', 'w') as archivo:
            for mision in self.misiones_obj:
                archivo.write(f"Misión {mision.nombre_mision}:\n")
                archivo.write(f"  Planeta destino: {mision.planeta_destino}\n")
                archivo.write(f"  Nave utilizada: {mision.nave_utilizar}\n")
                archivo.write(f"  Armas utilizadas: {', '.join(mision.armas_utilizar)}\n")
                archivo.write(f"  Integrantes: {', '.join(mision.integrantes_mision)}\n\n")

    def cargar_misiones(self):
        misiones = []
        try:
            with open('misiones.txt', 'r') as archivo:
                lines = archivo.readlines()
                mision = {}
                for line in lines:
                    line = line.strip()
                    if line.startswith("Misión "):
                        if mision:
                            misiones.append(Mision(
                                nombre_mision=mision['nombre_mision'],
                                planeta_destino=mision['planeta_destino'],
                                nave_utilizar=mision['nave_utilizar'],
                                armas_utilizar=mision['armas_utilizar'],
                                integrantes_mision=mision['integrantes_mision']
                            ))
                            mision = {}
                        mision['nombre_mision'] = line[7:]
                    elif line.startswith("  Planeta destino: "):
                        mision['planeta_destino'] = line[19:]
                    elif line.startswith("  Nave utilizada: "):
                        mision['nave_utilizar'] = line[18:]
                    elif line.startswith("  Armas utilizadas: "):
                        mision['armas_utilizar'] = [arma.strip() for arma in line[19:].split(',')]
                    elif line.startswith("  Integrantes: "):
                        mision['integrantes_mision'] = [integrante.strip() for integrante in line[13:].split(',')]
                if mision:
                    misiones.append(Mision(
                        nombre_mision=mision['nombre_mision'],
                        planeta_destino=mision['planeta_destino'],
                        nave_utilizar=mision['nave_utilizar'],
                        armas_utilizar=mision['armas_utilizar'],
                        integrantes_mision=mision['integrantes_mision']
                    ))
            self.misiones_obj = misiones
        except FileNotFoundError:
            print("No se encontró el archivo de misiones.")

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



    def abrir_characters(self):
        with open('characters.csv', 'r') as csv_characters:
            reader = csv.reader(csv_characters)
            data = list(reader) 
        dict_characters = {row[1]: row[10] for row in data[1:]}  
        return dict_characters

    def graficos_personajes_planetas(self,dict_characters):
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
    
    def grafico_comp_naves(self):

        # Leer el CSV
        with open('starships.csv', mode='r') as file:
            reader = csv.DictReader(file)
            
            lengths = []
            cargo_capacities = []
            hyperdrive_ratings = []
            mglt_values = []
            names = []

            for row in reader:
                # Extraer y convertir los datos
                try:
                    length = float(row['length']) if row['length'] else 0
                    cargo_capacity = float(row['cargo_capacity']) if row['cargo_capacity'] else 0
                    hyperdrive_rating = float(row['hyperdrive_rating']) if row['hyperdrive_rating'] else 0
                    mglt = float(row['MGLT']) if row['MGLT'] else 0
                    
                    lengths.append(length)
                    cargo_capacities.append(cargo_capacity)
                    hyperdrive_ratings.append(hyperdrive_rating)
                    mglt_values.append(mglt)
                    names.append(row['name'])
                except ValueError:                    
                    print(f"Error al convertir los datos para la nave")       

        # Gráfico de Longitud de la Nave
        plt.figure(figsize=(12, 8))
        plt.barh(names, lengths, color='skyblue')
        plt.title('Longitud de la Nave')
        plt.xlabel('Longitud (metros)')
        plt.ylabel('Nombre de la Nave') 
        plt.yticks(fontsize=7)          
        plt.tight_layout()
        plt.show()

        # Gráfico de Capacidad de Carga
        plt.figure(figsize=(12, 8))
        plt.barh(names, cargo_capacities, color='salmon')
        plt.title('Capacidad de Carga')
        plt.xlabel('Capacidad de Carga (kg)')
        plt.ylabel('Nombre de la Nave')   
        plt.yticks(fontsize=7)           
        plt.tight_layout()
        plt.show()

        # Gráfico de Clasificación del Hiperimpulsor
        plt.figure(figsize=(12, 8))
        plt.barh(names, hyperdrive_ratings, color='lightgreen')
        plt.title('Clasificación del Hiperimpulsor')
        plt.xlabel('Clasificación del Hiperimpulsor')
        plt.ylabel('Nombre de la Nave')  
        plt.yticks(fontsize=7)       
        plt.tight_layout()
        plt.show()

        # Gráfico de MGLT
        plt.figure(figsize=(12, 8))
        plt.barh(names, mglt_values, color='gold')
        plt.title('MGLT')
        plt.xlabel('MGLT')
        plt.ylabel('Nombre de la Nave')   
        plt.yticks(fontsize=7)     
        plt.tight_layout()
        plt.show()

    def modificar_mision(self):
        
        if len(self.misiones_obj) == 0:
            print("No hay misiones para modificar")
            return

        print(" Misiones:")
        for i, mision in enumerate(self.misiones_obj):
            print(f"{i+1}.- {mision.nombre}")
        
        try:                    
            seleccionar_mision = int(input("Seleccione una mision para modificar: "))
            if seleccionar_mision not in range(1, len(self.misiones_obj)+1):
                raise Exception
        except:
            print("Opción no válida")
            return
        mision_seleccionada = self.misiones_obj[seleccionar_mision-1]

        print(f"""
        1. Eliminar armas
        2. Agregar armas
        3. Eliminar integrantes
        4. Agregar integrantes""")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion not in range(1, 5):
                raise Exception
        except:
            print("Opción no válida")
            return
        
        if opcion == 1:    
            # eliminar armas   
            while len(mision_seleccionada.armas_utilizar) > 0:              
                print("Armas de la misión:")
                for i, arma in enumerate(mision_seleccionada.armas_utilizar):
                    print(f"{i+1}.- {arma}")
                
                try:
                    seleccionar_arma = int(input("Seleccione un arma para eliminar (o 0 para cancelar): "))
                    
                    if seleccionar_arma == 0:
                        break
                    if seleccionar_arma not in range(1, len(mision_seleccionada.armas_utilizar)+1):
                        raise Exception
                    
                    mision_seleccionada.armas_utilizar.pop(seleccionar_arma-1)
                    print("Arma eliminada con éxito")

                except:
                    print("Opción no válida")
                    return                

        elif opcion == 2:
            # agregar armas   
            
            if len(mision_seleccionada.armas_utilizar) >= 7:
                print("No puedes agregar más armas")
                return   
                  
            armas = []
            with open('weapons.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
                next(reader) 
                for row in reader:
                    armas.append(row[1])
            
            print("Armas disponibles:")
            for i, arma in enumerate(armas):
                print(f"{i+1}. {arma}")                    

            while len(mision_seleccionada.armas_utilizar) < 7:
                try:
                    seleccionar_arma = int(input("Seleccione un arma para agregar (o 0 para cancelar): "))
                    
                    if seleccionar_arma == 0:
                        break
                    if seleccionar_arma not in range(1, len(armas)+1):
                        raise Exception            
                    
                    arma = armas[seleccionar_arma-1]
                    if arma in mision_seleccionada.armas_utilizar:
                        print("El arma ya está en la misión")
                        continue
                    
                    mision_seleccionada.armas_utilizar.append(arma)
                    print(f"Arma: {arma} agregada con éxito")

                except:
                    print("Opción no válida")
                    return                        

        elif opcion == 3:
            # eliminar integrantes
            while len(mision_seleccionada.integrantes_mision) > 0:
                print("\nIntegrantes de la misión:")
                for i, integrante in enumerate(mision_seleccionada.integrantes_mision):
                    print(f"{i+1}.- {integrante}")
                
                try:
                    seleccionar_integrante = int(input("Seleccione un integrante para eliminar (o 0 para cancelar): "))
                    
                    if seleccionar_integrante == 0:
                        break
                    if seleccionar_integrante not in range(1, len(mision_seleccionada.integrantes_mision)+1):
                        raise Exception
                    
                    mision_seleccionada.integrantes_mision.pop(seleccionar_integrante-1)
                    print("Integrante eliminado con éxito")

                except:
                    print("Opción no válida")
                    return           

        elif opcion == 4:
            # agregar integrantes

            if len(mision_seleccionada.integrantes_mision) >= 7:
                print("No puedes agregar más integrantes")
                return

            personajes = []
            with open('characters.csv', 'r') as csv_file:
                reader = csv.reader(csv_file)
                next(reader) 
                for row in reader:
                    personajes.append(row[1])  

            print("Personajes disponibles:")
            for i, character in enumerate(personajes):
                print(f"{i+1}. {character}")
            
            while len(mision_seleccionada.integrantes_mision) < 7:
                try:
                    seleccionar_personaje = int(input("Seleccione un personaje para agregar (o 0 para cancelar): "))
                    
                    if seleccionar_personaje == 0:
                        break
                    if seleccionar_personaje not in range(1, len(personajes)+1):
                        raise Exception

                    personaje = personajes[seleccionar_personaje-1]
                    if personaje in mision_seleccionada.integrantes_mision:
                        print("El personaje ya está en la misión")
                        continue

                    mision_seleccionada.integrantes_mision.append(personaje)
                    print(f"Integrante: {personaje} agregado con éxito")

                except:
                    print("Opción no válida")
                    return                    
