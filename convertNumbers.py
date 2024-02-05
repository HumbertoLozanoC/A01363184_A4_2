'''
This program converts the 
numbers to binary and hexadecimal base

'''
import os
import time
from decimal import Decimal, InvalidOperation
import argparse

def decimal_to_hexadecimal(decimal_value):
    if decimal_value == 0:
        return '0'

    hex_chars = '0123456789ABCDEF'
    result = ''

    while decimal_value > 0:
        remainder = decimal_value % 16
        result = hex_chars[int(remainder)] + result
        decimal_value //= 16

    return result

def convert_to_hexadecimal_and_print(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

        # Procesar los valores en el archivo
        for line in content:
            try:
                value = Decimal(line.strip())
                hexadecimal_value = decimal_to_hexadecimal(value)
                print(f"Número decimal: {value}")
                print(f"Representación hexadecimal: {hexadecimal_value}")
                print("\n")
            except InvalidOperation:
                # Ignora líneas que no se pueden convertir a Decimal
                continue

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convierte números decimales a hexadecimales a partir de un archivo de datos.")
    parser.add_argument("file_path", metavar="file_path", type=str, help="Ruta del archivo con datos")

    args = parser.parse_args()
    file_path = args.file_path

    if os.path.isfile(file_path):
        Start_time = time.time()
        convert_to_hexadecimal_and_print(file_path)
        End_time = time.time()
        Execution_time = End_time - Start_time
        print("Tiempo de ejecución:", Execution_time, "segundos")
    else:
        print(f"El archivo {file_path} no es válido.")

