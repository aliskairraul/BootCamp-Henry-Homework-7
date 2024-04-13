from typing import Union

arbol_list: list = []


class Node:
    def __init__(self, dato: int) -> None:
        self.dato: int = dato
        self.left: id = None
        self.right: id = None
        # Parametro a usar para registrar posicion dentro del arbol
        self.level: int = None
        # Parametro a usar para registrar posicion dentro del arbol
        self.row_index: int = None


class BinaryTree:
    def __init__(self) -> None:
        """Metodo que inicia el Arbol binario"""
        self.root: id = None
        self.pointer: id = None
        self.level_max: int = 0

    def is_empty(self) -> bool:
        """Metodo para saber si el arbol esta vacio

        Returns:
            bool: Retorna True si el arbol está Vacio,
                  de lo contrario False
        """
        return True if self.root is None else False

    def insert(self, dato: int) -> None:
        """Inserta un nuevo dato en el arbol

        Args:
            dato (int): dato a insertar en el arbol
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
        """metodo para saber si un valor está en el arbol

        Args:
            dato (int): dato a buscar en el arbol

        Returns:
            bool: devuelve True si lo encuentra
                  o False en caso contrario
        """
        if self.is_empty():
            return False
        pointer = self.root
        while True:
            if pointer is None:
                return False
            if dato <= pointer.dato:
                # print('entro <=')
                pointer = pointer.left
            else:
                # print('entro else')
                pointer = pointer.right
            if pointer and pointer.dato == dato:
                return True

    def show(self) -> None:
        """Muestra los elementos de la lista

        Returns:
            _type_: Imprime 'IS EMPTY' si la lista esta vacia
                    en caso contrario llama a _show() quien
                    se ejecutara recursivamente para recorrer el arbol
        """
        if self.is_empty():
            return print("IS EMPTY")
        self._show(self.root)

    def _show(self, pointer: id, level: int = 0) -> None:
        """Recorre el arbol recursivamente y va imprimiendo los datos
           que estan en los nodos

        Args:
            pointer (id): Apuntador para recorrido. Empieza en root
            level (int, optional): Profundidad en el arbol. Empieza en 0
                                   Defaults to 0.
        """
        print(f"level {level}")  # Imprime el nivel de profundidad
        print(pointer.dato)
        if pointer.left:
            self._show(pointer.left, level=level + 1)
        if pointer.right:
            self._show(pointer.right, level=level + 1)

    def orden_arbol(self) -> None:
        """Se encarga de verificar que el arbol no esté vacio y en caso
        contrario apuntar a root y apoyarse en la funcion recursiva
        armar_diccionario para crear la lista de diccionarios para
        renderizar graficamente a el arbol binario
        """
        arbol_list.append({"Nodo": self.root.dato, "level": 0, "index": 0})
        self.armar_diccionario(self.root, level=0, row_index=0)

    def armar_diccionario(
        self, pointer: id, level: int = 0, row_index: int = 0
    ) -> None:
        """Recorre todo el arbol y arma una lista de Diccionarios con datos
           como el Nivel de profundidad indice dentro del nivel a la hora de
           renderizar por pantalla,  etc

        Args:
            pointer (id): Apuntador del nodo que llamo a la funcion
            level (int, optional): Nivel de profundidad del nodo que llama a la
                                   funcion. Defaults to 0.
            row_index (int, optional): Index dentro del nivel del nodo que llama a
                                       la funcion.  Este indice es la posicion para
                                       el renderizado. Defaults to 0.
        """
        if pointer.left:
            index = (row_index * 2) + 0
            arbol_list.append(
                {"Nodo": pointer.left.dato, "level": (level + 1), "index": index}
            )
            self.armar_diccionario(pointer.left, level + 1, index)
        if pointer.right:
            index = (row_index * 2) + 1
            arbol_list.append(
                {"Nodo": pointer.right.dato, "level": (level + 1), "index": index}
            )
            self.armar_diccionario(pointer.right, level + 1, index)
