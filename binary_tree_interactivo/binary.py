from typing import Union


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
