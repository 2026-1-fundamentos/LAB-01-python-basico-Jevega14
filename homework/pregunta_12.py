"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from ._data import read_rows


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    totals = {}
    for row in read_rows():
        row_total = sum(int(item.split(":")[1]) for item in row[4].split(","))
        totals[row[0]] = totals.get(row[0], 0) + row_total
    return dict(sorted(totals.items()))
