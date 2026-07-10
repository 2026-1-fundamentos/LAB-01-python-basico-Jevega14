"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from ._data import read_rows


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return sum(int(row[1]) for row in read_rows())
