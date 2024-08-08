import csv

class Weapon:
    def abrir_weapons(self):
            with open('weapons.csv', 'r') as csv_weapons:
                reader = csv.reader(csv_weapons)
                lista_csv_weapons = []             
                for row in reader:
                        lista_csv_weapons.append(row[1])  
            
    def __init__(self, name):
          self.name=name


