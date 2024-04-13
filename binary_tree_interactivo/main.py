import sys

# BinaryTree --> es la Estructura Arbol Binario (es una Clase)
# render_tree --> es la función que se encarga de dibujar en pantalla (es una Función)
from binary_tree import BinaryTree, render_tree

from utiles import Utiles

utiles = Utiles()
tree = BinaryTree()
response: str
number: int


def main() -> None:
    first_time: bool = True
    while True:
        if not first_time:
            render_tree(tree_list=tree.tree_list_)
        if first_time:
            utiles.clear_screen()
        utiles.blanK_lines(10)
        print(" " * 40, "BINARY TREE")
        utiles.blanK_lines(4)
        print("  Please insert a node")
        print('  Note: Only [0-99] integer numbers, or "Q" to exit')
        response = input("  Node --> ")

        if response.strip().upper() == "Q":
            sys.exit(0)

        if not response.strip().isdigit() or int(response.strip()) > 99:
            utiles.blanK_lines(2)
            input("ENTRADA NO VALIDA")
            continue

        first_time = False
        number = int(response.strip())
        tree.insert(number)
        tree.tree_order()


if __name__ == "__main__":
    main()
