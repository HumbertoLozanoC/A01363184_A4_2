'''
This program calculates statics like the mean, median, mode, standard deveation, and variance

'''

import os
import time
from decimal import Decimal, InvalidOperation
import argparse

def compute_statistics(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

        # Procesar los valores en el archivo
        values = []  # Inicializa la lista de valores
        addition = Decimal(0)

        for line in content:
            try:
                value = Decimal(line.strip())
                values.append(value)  # Agrega el valor a la lista
                addition += value
            except InvalidOperation:
                # Ignora líneas que no se pueden convertir a Decimal
                continue

        if values:
            Count = len(values) 
            media = addition / Count
            datos_ordenados = sorted(values)
            longitud = len(datos_ordenados)

            if longitud % 2 == 0:
                        mediana = (datos_ordenados[longitud // 2 - 1] + datos_ordenados[longitud // 2]) / 2
            else:
                        mediana = datos_ordenados[longitud // 2]
            
            frecuencias = {}
            for value in values:
                        frecuencias[value] = frecuencias.get(value, 0) + 1

            moda = max(frecuencias, key=frecuencias.get)

            Suma_de_cuadrados = sum((x - media) ** 2 for x in values)
            Desviacion_standar = (Suma_de_cuadrados / Count).sqrt()

            print(f"Archivo: {file_path}")
            print("Media:", media)
            print("Mediana:", mediana)
            print("Moda:", moda)
            print("Count:", Count)
            print("Desviacion estandar", Desviacion_standar)
            print("\n")
        else:
            print(f"Archivo: {file_path} no contiene valores válidos.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calcula estadísticas a partir de un archivo de datos.")
    parser.add_argument("file_path", metavar="file_path", type=str, help="Ruta del archivo con datos")

    args = parser.parse_args()
    file_path = args.file_path

    if os.path.isfile(file_path):
        Start_time = time.time()
        compute_statistics(file_path)
        End_time = time.time()
        Execution_time = (End_time - Start_time) * 1000
        print("Tiempo de ejecución:", Execution_time, "milisegundos")
    else:
        print(f"El archivo {file_path} no es válido.")

