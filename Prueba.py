from Mision import Mision
import csv


def crear_mision(self):
    num_misiones = 0
    print("Creemos una nueva misión")
    
    while num_misiones < 5:
        nombre_mision = input("Ingrese el nombre de la mision: ")

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

        if num_misiones < 5:
            respuesta = input("¿Desea crear otra misión? (si/no): ")
            if respuesta.lower() == 'no':
                break
    else:
        print("Se han creado 5 misiones. No se pueden crear más.")