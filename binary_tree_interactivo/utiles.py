import os
import logging


class Utiles:
    def __init__(self) -> None:
        pass

    def verificar_existe(self, path_file: str, header: str = None) -> None:
        """Comprueba si un archivo  existe y de no existir lo crea y añade
        los encabezados de columnas si el parametro header no es None

        Args:
            path_file (str): path del archivo
            header (str, optional): encabezado de columnas.  Defaults to None.
        """
        if header is None:
            header = ""
        if not os.path.exists(path_file):
            archivo = open(path_file, "w", encoding="utf-8")
            archivo.write(header)
            archivo.close()

    def clear_screen(self) -> None:
        """Limpia la pantalla de la terminal"""
        os.system("cls" if os.name == "nt" else "clear")

    def blanK_lines(self, number: int) -> None:
        """Imprime lineas vacias en la Terminal

        Args:
            number (int): numero de lineas en blanco
        """
        for i in range(number):
            print("")
