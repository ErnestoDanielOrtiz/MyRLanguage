# MyRLanguage

Proyecto para la clase Diseño de Compiladores

Manual de usuario
Para utilizar el lenguaje myR, primero hay que asegurarse de tener installado lark. Esto se hace de la manera siguiente: pip install lark
Una vez que se tiene lark, se ejecuta el código de main.py. Dentro de este archivo se encuentra el código de cual es el archivo que se quiere compilar, por lo que hay que tener mucho cuidado con las rutas hacia el archivo y los nombres para que este funcione correctamente.

Avance 1
Se creo el la gramática con sus reglas. Se imprimen las reglas al probar el codigo.
Aparecen "errores" en lineas "que no existen". 1352, 1203, 1084, 1062.

Avance 2
Se agregaron las clases Variable y VariableTable, que sirven para meterlas a la tabla de variables, asi como buscar si existen y regresarlas si son llamadas.
Se creo el cubo semantico
Falta hacer pruebas, se haran en los siguientes 2 dias.

Avance 3
No pude avanzar debido a problemas externos.

Avance 4
Se tienen clases de funcion, directorio de funciones y puntos neuralgicos.
Se agrego la clase cuadruplos que imprime estos en un archivo de texto.

Avance 5
Se agregaron cuadruplos de condicionales

Avance 6
Se creo la memoria virtual con las direcciones
Se crearon puntos neuralgicos
Se cambio un poco la gramatica
