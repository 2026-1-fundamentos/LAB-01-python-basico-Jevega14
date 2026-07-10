"""Utilidades compartidas para leer los datos del laboratorio."""

from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent.parent / "files" / "input" / "data.csv"


def read_rows():
    """Retorna las filas del archivo separadas en sus cinco columnas."""
    with DATA_FILE.open(encoding="utf-8") as data_file:
        return [line.rstrip("\n").split("\t") for line in data_file if line.strip()]

