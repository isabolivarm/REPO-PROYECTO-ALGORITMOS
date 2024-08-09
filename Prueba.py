
import csv

weapons = []
with open('weapons.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # saltar la fila de headers
    for row in reader:
        weapons.append(row[1])  # agregar solo el nombre de la arma

print("Armas disponibles:")
for i, weapon in enumerate(weapons):
    print(f"{i+1}. {weapon}")

selected_weapons = []
while len(selected_weapons) < 7:
    eleccion = int(input("Ingrese el número de la arma que desea seleccionar (o 0 para finalizar): "))
    if eleccion == 0:
        break
    selected_weapons.append(weapons[eleccion-1])
    print(f"Ha seleccionado: {selected_weapons[-1]}")

print("Armas seleccionadas:")
for weapon in selected_weapons:
    print(weapon)