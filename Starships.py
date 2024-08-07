import csv
def abrir_naves():
    with open("starships.csv","r") as archivo_starships:
        reader=csv.reader(archivo_starships)
        hiper_impulsores=[]
        mglt=[]
        velocidad_maxima=[]
        costo_credito=[]
        for row in reader:
            hiper_impulsores.append(row[12])
            mglt.append(row[13])
            velocidad_maxima.append(row[7])
            costo_credito.append(row[5])
abrir_naves()

