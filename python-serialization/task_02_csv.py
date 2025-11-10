#!/usr/bin/env python3
"""Module that converts a CSV file to JSON."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON format and save it as data.json."""
    try:
        # Abrimos el CSV en modo lectura
        with open(filename, 'r', newline='') as csv_file:
            # DictReader convierte cada fila del CSV en un diccionario
            reader = csv.DictReader(csv_file)
            data = list(reader)  # Convertimos el objeto reader en una lista de diccionarios

        # Abrimos (o creamos) el archivo JSON en modo escritura
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)  # indent=4 para que se vea bonito

        return True  # Éxito

    except FileNotFoundError:
        # Si el archivo CSV no existe, retornamos False
        return False

    except Exception:
        # Cualquier otro error general
        return False
