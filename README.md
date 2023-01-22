# prepexamen.py
https://github.com/Jaimerpb/prepexamen.py.git

#Ej4_1ºconv
# Su tarea es escribir una función llamada do_math que reciba un solo argumento. 
# Este argumento es una cadena que contiene varios números delimitados por espacios en blanco. 
# Cada número tiene una sola letra del alfabeto en algún lugar dentro de él.

# Ejemplo: "24z6 1x23 y369 89a 900b"

# Como se muestra arriba, esta letra del alfabeto puede aparecer en cualquier lugar dentro del número. 
# Tienes que extraer las letras y ordenar los números según sus letras correspondientes.


# Aquí viene la parte difícil, ahora tienes que hacer una serie de cálculos sobre los números que has extraído.

# La secuencia de cálculos es + - * /. 
# Las reglas matemáticas básicas NO se aplican, debe hacer cada cálculo exactamente en este orden.
# Esto tiene que funcionar para cualquier tamaño de números enviados (después de la división, volver a la suma, etc.).
# En el caso de letras del alfabeto duplicadas, debe organizarlas de acuerdo con el número que apareció primero en la cadena de entrada.
# Recuerde también redondear la respuesta final al entero más cercano.
# Puedes escribir una función llamada do_math que realice los cálculos descritos en el enunciado del problema. La función debería tomar una sola cadena como argumento y devolver un número entero como resultado. Para resolver el problema, la función puede seguir los siguientes pasos:

# Separe la cadena de entrada en una lista de números utilizando el espacio como separador.
# Para cada número en la lista, extraiga la letra del alfabeto que se encuentra en el número y almacénela en un diccionario junto con el número entero correspondiente.
# Ordenar el diccionario según las letras del alfabeto que se han extraído de los números.
# Realizar los cálculos especificados en el enunciado utilizando los números ordenados del diccionario. Redondear el resultado final al entero más cercano y devolverlo como resultado de la función.
# Ejemplos:

# "24z6 1x23 y369 89a 900b" = 89 + 900 - 123 * 369 / 246 = 1299

# "24z6 1z23 y369 89z 900b" = 900 + 369 - 246 * 123 / 89 = 1414

# "10a 90x 14b 78u 45a 7b 34y" = 10 + 45 - 14 * 7 / 78 + 90 - 34 = 60

# ¡Buena suerte y que el CÓDIGO te acompañe!
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-> Ejercicios Python-Tema3.pdf
EJERCICIO: COMPARA LOS PROBLEMAS
Lucía y Carlos crearon cada uno un problema para su posterior calificación.
Un revisor califica los dos problemas, otorgando puntos en una escala del 1 al 100 para tres
categorías: claridad del problema, originalidad y dificultad .
La calificación del desafío de Lucía es el desafío a = (a [0], a [1], a [2]), y la calificación del desafío de
Carlos es el desafío b = (b [0], b [1], b [2]) .
La tarea consiste en encontrar sus puntos de comparación comparando a [0] con b [0] , a [1] con b
[1] y a [2] con b [2] .
Si a [i]> b [i] , entonces Lucía recibe 1 punto.
Si a [i] <b [i] , entonces Carlos recibe 1 punto.
Si a [i] = b [i] , ninguna persona recibe un punto.
Los puntos de comparación son los puntos totales que ganó una persona.
Dada una a y b , determinar sus respectivos puntos de comparación.
Para los elementos * 0 *, Carlos recibe un punto debido a un [0].
Para los elementos iguales a [1] y b [1] , se consiguen sin puntos.
Finalmente, para los elementos 2 , a [2]> b [2] por lo que Lucía recibe un punto.
La matriz de retorno es [1, 1] con la puntuación de Lucía primero y la de Carlos en segundo lugar.
Función descriptiva
Complete la función compareTriplets . compareTriplets tiene los siguientes parámetros:
int a [3] : calificación de desafío de Lucía
int b [3] : calificación de desafío de Carlos
Salida
int [2] : la puntuación de Alice está en la primera posición y la puntuación de Bob en la segunda.
Formato de entrada
La primera línea contiene 3 números enteros separados por espacios, un a[0] , un a[1] y un a[2] , los
valores respectivos al desafío a .
La segunda línea contiene 3 números enteros separados por espacios, b [0] , b [1] , y b [2] , los valores
respectivos al desafío b .
Código Proporcionado
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
# 1. INTEGER_ARRAY a
# 2. INTEGER_ARRAY b
#
def compareTriplets(a, b):
# Write your code here
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ej9_1ºconv
# ¡A nadie le gustan los lunes! Pasaste el fin de semana de fiesta y con amigos, y luego llega el lunes y tienes que levantarte temprano, ponerte ropa de negocios e ir a trabajar. Entonces, ¿cuántos de estos horribles días tiene que soportar alguien? Bueno, averigüémoslo.

# Cree un método para encontrar el número de lunes dado el cumpleaños de una persona y la fecha actual. Para este ejercicio simple, no te preocupes por los días festivos/vacaciones, licencia por enfermedad, etc. Supongamos que una persona tiene un trabajo y va a trabajar durante todo el año si está en edad de trabajar. Para simplificar las cosas, suponga que alguien comienza a trabajar cuando tiene 22 años y se jubila cuando tiene 78.

# ¡Así es, los lunes no cuentan cómo días malos si estás en la escuela/universidad o eres jubilado!

# En las pruebas, la fecha actual será la misma o posterior al cumpleaños de una persona y ambas fechas serán no nulas y válidas. Y aunque no tener que trabajar los fines de semana es una moda bastante reciente (¡búscalo!), asume que los lunes siempre serán y serán días malos en cualquier época.

# Para resolver este problema, se puede seguir los siguientes pasos:

# Calcular la edad de la persona en la fecha actual. Para ello, se puede calcular la diferencia en años entre la fecha actual y la fecha de cumpleaños de la persona.
# Verificar si la persona está en edad de trabajar. Para ello, se puede comprobar si su edad está entre 22 y 78 años.
# Calcular el número de lunes que hay entre la fecha de cumpleaños y la fecha actual. Para ello, se puede calcular el número de días que hay entre ambas fechas y dividirlo por 7, ya que una semana tiene 7 días.
# Si la persona está en edad de trabajar, devolver el número de lunes calculado en el paso 3. En caso contrario, devolver 0.