#estas son las librerias o extensiones que se necesitan para poder graficar el programa y para darle la aleatoreidad
import random
import matplotlib.pyplot as plt

##esta función simula la caída de un número específico de bolas a través de una Máquina de Galton con un número determinado de compartimentos,
#  registrando cuántas bolas caen en cada compartimento. La distribución resultante se reflejará en la lista slots.
def galton_machine(num_balls, num_slots):
    slots = [0] * (num_slots + 1)

    for _ in range(num_balls):
        position = num_slots // 2
        for _ in range(num_slots):
            direction = random.choice([-1, 1])
            position += direction

           # es neceserio asegurarse de que position esté dentro de los límites de la lista o de lo contrario no podra funcionar y puede ser un error muy 
            # poco preceptible pero vital para que el programa funcione yo lo descubri de mala manera coloque el +=1 solo y non me dejaba seguir 
            position = max(0, min(position, num_slots))

        slots[position] += 1

    return slots

  #Esta función toma la distribución generada por la función galton_machine 
  # La distribución es la lista slots que contiene el recuento de bolas en cada compartimento después de la simulación.
  # no supe que valor tomar para medir la cantidad maxima de canicas en cada slot pero marque el 700 como limite espero ese valor sirva

def plot_distribution(distribution):
    max_count = max(distribution)
    scale_factor = 100 / max_count

    bars = [count * scale_factor for count in distribution]

    plt.bar(range(len(bars)), bars)
    plt.xlabel('Celda')
    plt.ylabel('Conteo de bolas')
    plt.title('Distribucion Maquina de Galton')
    plt.show()
