# Abre el archivo en modo lectura
'''
Este programa se encarga de contar las veces que se repiten las palabras en un archivo de texto

'''
import os
import time
import argparse

def Count_words(file_path):
    # Inicializa un diccionario para almacenar las palabras y sus conteos
    word_count = {}

    # Abre el archivo en modo lectura
    with open(file_path, 'r') as file:
        # Recorre cada línea del archivo
        for line in file:
            # Divide la línea en palabras
            words = line.split()

            # Recorre cada palabra en la línea
            for word in words:
                # Elimina posibles caracteres especiales al inicio o final de la palabra
                word = word.strip(".,!?()[]{}\"'")

                # Convierte la palabra a minúsculas para evitar contar palabras iguales con diferente capitalización
                word = word.lower()

                # Incrementa el conteo de la palabra en el diccionario
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    # Imprime el resultado
    for word, count in word_count.items():
        print(f'{word}: {count}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cuenta el número de veces que se repite una palabra a partir de un archivo de datos")
    parser.add_argument("file_path", metavar="file_path", type=str, help="Ruta del archivo con datos")

    args = parser.parse_args()
    file_path = args.file_path

    if os.path.isfile(file_path):
        Start_time = time.time()
        Count_words(file_path)
        End_time = time.time()
        Execution_time = (End_time - Start_time) * 1000
        print("Tiempo de ejecución:", Execution_time, "milisegundos")
    else:
        print(f"El archivo {file_path} no es válido.")

