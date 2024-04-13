from typing import Union
from utiles import Utiles
import pandas as pd

utiles = Utiles()
separators: list = [
    "┌────────────────────────────┴───────────────────────────┐",
    "┌───────────┴───────────┐",
    "┌─────┴─────┐",
    "┌───┴───┐",
]
blank_spaces: list = [58, 25, 13, 9]


class Node:
    def __init__(self, dato: int) -> None:
        """Clase Node que es la unidad minima del Arbol

        Args:
            dato (int): Inf que se guardara en el Nodo
        """
        self.dato: int = dato
        self.left: object = None
        self.right: object = None
        self.level: int = None
        self.row_index: int = None


class BinaryTree:
    def __init__(self) -> None:
        """Estructura que guarda todos los metodos del Arbol binario"""
        self.root: id = None
        self.pointer: id = None
        self.level_max: int = 0
        self.tree_list_: list = []

    def is_empty(self) -> bool:
        """Para Verificar si el Arbol contiene al menos 1 Nodo

        Returns:
            bool: Verdarero si esta vacio o falso de lo contrario
        """
        return True if self.root is None else False

    def insert(self, dato: int) -> None:
        """Permite el ingreso de nuevos Nodos al Arbol

        Args:
            dato (int): Informacion a guardarse en el Nodo
        """
        if self.is_empty():
            self.root = Node(dato)
            return
        self.pointer = self.root
        while True:
            if dato <= self.pointer.dato:
                if self.pointer.left is None:
                    self.pointer.left = Node(dato)
                    return
                else:
                    self.pointer = self.pointer.left
            else:
                if self.pointer.right is None:
                    self.pointer.right = Node(dato)
                    return
                else:
                    self.pointer = self.pointer.right
            self.level_max += 1

    def found(self, dato: int) -> bool:
        """Metodo para encontrar un valor en el arbol

        Args:
            dato (int): Valor a Buscar dentro del arbol

        Returns:
            bool: Verdadero si lo encontro, Falso en caso contrario
        """
        if self.is_empty():
            return False
        pointer = self.root
        while True:
            if pointer is None:
                return False
            if dato <= pointer.dato:
                pointer = pointer.left
            else:
                pointer = pointer.right
            if pointer and pointer.dato == dato:
                return True

    def show(self) -> None:
        """Mostrar los nodos de un arbol
           Se apoya en el metodo show_

        Returns:
            _type_: Imprimira en pantalla que esta vacio si es el caso
                    si no imprime la pantalla a root y llama a show_
        """
        if self.is_empty():
            return print("IS EMPTY")
        self.show_(self.root)

    def show_(self, pointer: id, level: int = 0) -> None:
        """recorrera el arbol de manera recursiva e imprimira los datos
           contenidos en cada Nodo

        Args:
            pointer (id): Apuntador del nodo que llama a la funcion recursiva
            level (int, optional): Indica el nivel de profundidad del nodo
                                   que llama a la funcion recursiva.
        """
        print(f"level {level}")
        print(pointer.dato)
        if pointer.left:
            self.show_(pointer.left, level=level + 1)
        if pointer.right:
            self.show_(pointer.right, level=level + 1)

    def tree_order(self) -> None:
        """Se encarga de verificar que el arbol no esté vacio y
        en caso contrario apuntar a root y apoyarse en la funcion
        recursiva armar_diccionario para crear la lista de
        diccionarios para renderizar graficamente a el arbol binario
        """
        self.tree_list_ = []
        self.tree_list_.append({"Nodo": self.root.dato, "level": 0, "index": 0})
        self.create_list_of_dicts(pointer=self.root, level=0, row_index=0)

    def create_list_of_dicts(
        self, pointer: id, level: int = 0, row_index: int = 0
    ) -> None:
        """Recorre todo el arbol y arma una lista de Diccionarios con datos como
           el Nivel de profundidad indice dentro del nivel a la hora de
           renderizar por pantalla,  etc

        Args:
            pointer (id): Apuntador al nodo cuya inf será utilizada para crear
                          un Diccionario que se agregara a la lista
            level (int, optional): Nivel de Profundidad que tiene el apuntador
                                   del nodo Padre que llama a la funcion recursiva
            row_index (int, optional): Indice del Nodo padre dentro de la pseudo
                                       matriz de renderizado. El indice del nodo
                                       Actual se calcula (indice_padre * 2 + 0)
                                       si es hijo izquierdo y (indice_padre * 2 + 1)
                                       si es un hijo derecho
        """
        if pointer.left:
            index = (row_index * 2) + 0
            self.tree_list_.append(
                {"Nodo": pointer.left.dato, "level": (level + 1), "index": index}
            )
            self.create_list_of_dicts(pointer.left, level + 1, index)
        if pointer.right:
            index = (row_index * 2) + 1
            self.tree_list_.append(
                {"Nodo": pointer.right.dato, "level": (level + 1), "index": index}
            )
            self.create_list_of_dicts(pointer.right, level + 1, index)


# FINAL DE LA class BinaryTree

# PRINCIPIO DE LAS FUNCIONES DE RENDERIZADO


def show_tree(show_list: list, separ_list: list, depth: int) -> None:
    """Renderiza el abol

    Args:
        show_list (list): lista de lista con los valores a mostrar
                          en el arbol
        separ_list (list): lista con los separadores o espacios en
                           blancos a mostrar
        depth (int): profundidad que tiene el arbol a mostrar
    """
    utiles.clear_screen()
    utiles.blanK_lines(4)
    # LEVEL 0
    if depth >= 0:
        print(" " * 53, show_list[0][0])
        print(" " * 25, separ_list[0][0])
    # LEVEL 1
    if depth >= 1:
        print(" " * 24, show_list[1][0], " " * 53, show_list[1][1])
        print(" " * 13, separ_list[1][0], " " * 30, separ_list[1][1])
    # LEVEL 2
    if depth >= 2:
        print(
            " " * 12,
            show_list[2][0],
            " " * 20,
            show_list[2][1],
            " " * 29,
            show_list[2][2],
            " " * 20,
            show_list[2][3],
        )
        print(
            " " * 7,
            separ_list[2][0],
            " " * 9,
            separ_list[2][1],
            " " * 18,
            separ_list[2][2],
            " " * 9,
            separ_list[2][3],
        )
    # LEVEL 3
    if depth >= 3:
        print(
            " " * 6,
            show_list[3][0],
            " " * 8,
            show_list[3][1],
            " " * 8,
            show_list[3][2],
            " " * 8,
            show_list[3][3],
            end="",
        )
        print(
            " " * 18,
            show_list[3][4],
            " " * 8,
            show_list[3][5],
            " " * 8,
            show_list[3][6],
            " " * 8,
            show_list[3][7],
        )
        print(
            " " * 3,
            separ_list[3][0],
            " ",
            separ_list[3][1],
            " ",
            separ_list[3][2],
            " ",
            separ_list[3][3],
            end="",
        )
        print(
            " " * 11,
            separ_list[3][4],
            " ",
            separ_list[3][5],
            " ",
            separ_list[3][6],
            " ",
            separ_list[3][7],
        )
    # LEVEL 4
    if depth >= 4:
        print(
            " " * 2,
            show_list[4][0],
            " " * 4,
            show_list[4][1],
            " ",
            show_list[4][2],
            " " * 3,
            show_list[4][3],
            end="",
        )
        print(
            " ",
            show_list[4][4],
            " " * 4,
            show_list[4][5],
            " ",
            show_list[4][6],
            " " * 4,
            show_list[4][7],
            end="",
        )
        print(
            " " * 9,
            show_list[4][8],
            " " * 4,
            show_list[4][9],
            " ",
            show_list[4][10],
            " " * 3,
            show_list[4][11],
            end="",
        )
        print(
            "  ",
            show_list[4][12],
            " " * 3,
            show_list[4][13],
            "",
            show_list[4][14],
            " " * 4,
            show_list[4][15],
        )


def render_tree(tree_list: list) -> None:
    utiles.clear_screen()
    """Adecua dimensiones, y Asigna valores correspondientes a las 
       show_list (donde se encuentran los valores de los nodos) y a
       separators_list (donde se encuentran los separadores o espacios 
       en blanco correspondientes), para renderizar (imprimir en 
       consola) con la funcion show_tree()

      Variables a Considerar:
        depth -> VARIABLE A UTILIZAR PARA LA PROFUNDIDAD DEL ARBOL  
        show_list -> LISTA CON LOS ELEMENTOS VISUALES NODOS A MOSTRAR
        separ_list -> LISTA CON LOS ELEMENTOS VISUALES SEPARADORES A MOSTRAR

    """

    depth: int = 0
    show_list: list = [["  "]]
    separ_list: list = [[""]]
    # ME APOYO EN UN DATAFRAME PARA QUE ME ORDENE POR NIVEL E INDEX
    utiles.blanK_lines(4)
    df = pd.DataFrame(tree_list).sort_values(["level", "index"])

    # NECESITO LA PROFUNDIDAD DEL ARBOL PARA CREAR LA LISTA SHOW ó MOSTRAR
    depth = df["level"].max()

    # AMPLIO la LISTA DE LISTAS, LLENA DE BLANCOS '  ' (show_list) CON LOS
    # ESPACIOS JUSTOS ES DECIR LA LISTA QUE REPRESENTA CADA
    # NIVEL TENDRA 2^depth POSICIONES
    show_list = [["  "]]
    separ_list = [["  "]]
    for i in range(1, (depth + 1)):
        show_list.append([])
        separ_list.append([])
        for j in range(2 ** (i)):
            show_list[i].append("  ")
            # APROVECHO AMPLIAR TAMBIEN LA LISTA DE LISTAS QUE
            # CONTIENEN LOS SEPARADORES VISUALES
            separ_list[i].append("  ")

    # RELLENO LA LISTA show_list CON LOS VALORES QUE DEBEN IR EN CADA
    # POSICION, O '  ' SI NO HAY VALOR PARA LA MISMA
    # ESOS VALORES ME LOS DA EL DF CON LAS COLUMNAS level y row_index
    for row in range(df.shape[0]):
        i = df["level"][row]
        j = df["index"][row]
        show_list[i][j] = (
            str(df["Nodo"][row])
            if len(str(df["Nodo"][row])) == 2
            else "0" + str(df["Nodo"][row])
        )

    for i in range(depth + 1):
        if i < 4:
            for j in range(len(show_list[i])):
                separ_list[i][j] = (
                    separators[i] if show_list[i][j] != "  " else " " * blank_spaces[i]
                )

    show_tree(show_list=show_list, separ_list=separ_list, depth=depth)
    return
