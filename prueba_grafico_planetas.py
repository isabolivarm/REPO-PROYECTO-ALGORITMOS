import matplotlib.pyplot as plt
import csv

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