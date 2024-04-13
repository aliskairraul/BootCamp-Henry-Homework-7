# Arbol Binario

<p style="text-indent: 40px;">Este repositorio está dedicado a compartir el algoritmo realizado en el Homework 7 del Modulo I del Bootcamp de Henry en la especialidad de Data Science. El algoritmo pedido debia ser una estructura de Datos tipo Arbol Binario, que cumpliera con la condición de que el primer Nodo Introducido se fijara como el Root, y de allí en adelante, los siguiente nodos introducidos por el usuario debían ser evaluados y los `menores o iguales` ir asignandolos hacia la rama izquierda y los mayores a la derecha <br></p>
<p style="text-indent: 40px;">El repositorio en si consta de dos(2) carpetas: </p>

- /mod1_homw7_henry/
  - **/mod1_homw7_henry/binary_tree_homework.py** --> Estructura de Datos
  - **/mod1_homw7_henry/homework_m1.ipynb** --> Cuaderno de Jupyter donde se importa la estructura de datos y se realizan las pruebas
- /binary_tree_interactivo/

  - **/binary_tree_interactivo/binary_tree.py** --> Estructura de Datos y funciones de Renderizado
  - **/binary_tree_interactivo/utiles.py** --> Utilidades varias, como limpiar terminal, etc
  - **/binary_tree_interactivo/main.py** --> Archivo a ejecutar desde la teminal que despliega el menu principal de la app
    <br>
    <br>

  ### Requerimientos:

  - Jupyter
  - Pandas
  - Numpy
    <br>
    <br>

  ### Uso:

    <p style="text-indent: 40px;">Para utilizar el arbol binario interactivo, deberá abrir una terminal, ubicarse en la capeta <b>/binary_tree_interactivo/</b> y correr el achivo <b>main.py</b></p>

    <image  src='images/ejecutando_la_app.png'/>

    <p style="text-indent: 40px;">Una vez ejecutado el programa debe aparecer la siguiente pantalla</p>

    <image src='images/pantalla_inicial.png'>

    <p style="text-indent: 40px;">Despues de Varias Interacciones debe mostrarse el arbol con sus distintas ramificaciones... Por ejemplo, si ingresa los siguientes Nodos en el orden a continuación [50,80,30,20,10,90,70,40,60,75] deberia ver algo como la siguiente imagen</p>
    <image src='images/arbol_con_nodos.png'>

    <p style="text-indent: 40px;">La idea de la representación gráfica es solo probar el funcionamiento de la estructura de Datos <b>Arbol Binario</b>. Tomar en cuenta que por limitaciones de spacio en la terminal, la parte interactiva solo podrá mostrarse hasta el nivel de profundidad 4. De igual manera se valido para solo aceptar numeros entre 1 y 99 para poder manejarlos como cadenas de 2 espacios (a los numeros del 1 al 9 se les agrega un 0 al principio) esto con la finalidad de que no se descuadre el dibujo en la terminal</p>

### Autor:

Aliskair Rodríguez<br>
Henry Bootcamp Data Science<br>
Cohorte Data-PT10
