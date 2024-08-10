import csv
import statistics
import tabulate


class Starship:
    def abrir_naves():
        with open("starships.csv", "r") as archivo_starships:
            reader = csv.reader(archivo_starships)
            next(reader)
            hiper_impulsores = []
            mglt = []
            velocidad_maxima = []
            costo_credito = []
            nombres_starships = []
            for row in reader:
                if row[11]== '':  
                    hiper_impulsores.append(float(row[11]))
                else:
                    hiper_impulsores.append(0.0) 

                if row[12]== '':  
                    mglt.append(float(row[12]))
                else:
                    mglt.append(0.0)  

                if row[6]== '':  
                    velocidad_maxima.append(float(row[6]))
                else:
                    velocidad_maxima.append(0.0)  # Asigna un valor por defecto si es vacío

                if row[4]== '': 
                    costo_credito.append(float(row[4]))
                else:
                    costo_credito.append(0.0)  

                nombres_starships.append(row[1])  

        estadísticas_starships = {
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
        for nombre, stats in estadísticas_starships.items():
            fila = [nombre]
            for stat in estadisticas_nombres:
                fila.append(stats[stat])
            filas.append(fila)

    
        headers = ["Estadística", "Promedio", "Moda", "Máximo", "Mínimo"]
        print(tabulate.tabulate(filas, headers=headers, tablefmt="grid"))

    

    abrir_naves()