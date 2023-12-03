# HUGO_TAVIRAS_proyectoM3.py
ESTE PROYECTO para ser honesto no entendia bien como funcionaba sobre todo al usar las bibliotecas matplolib tuve errores porque se intalo en otra version de python y no terminaba de entender para que funcionaba el import random asi que me vi en la necesidad de buscar el fuentes externas ejemplos lo mas parecidos posibles para darme una idea de como se debia hacer pero la mayoria mostraban solo el resultado y no el proceso en si, creo que cumpli con los requisitos necesarios pero no supe si limitar la cantidad de bolas de cada compartimiento estaba bien o debia ser un valor que se determinara de manera aleatoria tambien pero si es el caso la verdad no supe como hacerlo 

Definición del Problema:
El objetivo del proyecto es simular la caída de bolas a través de una Máquina de Galton y visualizar la distribución resultante.

Estructura del codigo: Se creó una función galton_machine para simular la caída de bolas. La función toma dos parámetros: num_bolas (número de bolas a simular) y num_slots (número de compartimentos en la máquina).

Simulación de la Máquina de Galton: La función utiliza un bucle para simular la caída de cada bola. Para cada bola, se elige aleatoriamente una dirección (izquierda o derecha) en cada clavo y se actualiza la posición de la bola. Se asegura que la posición de la bola esté dentro de los límites válidos de los compartimentos de la máquina ademas se mantiene un contador para cada compartimento para registrar cuántas bolas han caído en cada uno.

Visualización con Matplotlib: Se utiliza la biblioteca matplotlib para visualizar la distribución resultante se crea una función plot_distribution que toma la distribución generada y crea un gráfico de barras para representar visualmente los resultados. Se proporcionan parámetros como num_bolas y num_slots para permitir la configuración flexible de la simulación.
Resultados:
El resultado final es un gráfico de barras que ilustra cómo se distribuyen las bolas en los compartimentos después de múltiples simulaciones.
Este proyecto utiliza conceptos como simulación, aleatoriedad y visualización para demostrar de manera práctica cómo funciona una Máquina de Galton y cómo evoluciona la distribución a medida que más bolas caen a través de ella.
