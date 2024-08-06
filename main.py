from App import App
import csv

def main(self):
    file_path="C:\Users\Gaby_\Downloads\starwars.zip\csv"
    with open (file_path,"r") as file:
        csv_reader=csv.reader(file)
        header=next(csv_reader)
        data=[row for row in csv_reader]

    print("Encabezado:",header)
    print("Primeras filas de datos: ",data[:5])
main()