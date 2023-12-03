##estas son las librerias o extensiones que se necesitan para poder graficar el programa y para darle la aleatoreidad
import random
import matplotlib.pyplot as plt

##esta función simula la caída de un número específico de bolas a través de una Máquina de Galton con un número determinado de compartimentos,
#  registrando cuántas bolas caen en cada compartimento. La distribución resultante se reflejará en la lista slots.
def galton_machine(num_bolas, num_slots):
    slots = [0] * (num_slots + 1)

    for _ in range(num_bolas):
        posicion = num_slots // 2
        for _ in range(num_slots):
            direction = random.choice([-1, 1])
            posicion += direction

            # es neceserio asegurarse de que position esté dentro de los límites de la lista o de lo contrario no podra funcionar y puede ser un error muy 
            # poco preceptible pero vital para que el programa funcione yo lo descubri de mala manera coloque el +=1 solo y non me dejaba seguir 
            posicion = max(0, min(posicion, num_slots))

        slots[posicion] += 1

    return slots
  #Esta función toma la distribución generada por la función galton_machine 
  # La distribución es la lista slots que contiene el recuento de bolas en cada compartimento después de la simulación.
  # no supe que valor tomar para medir la cantidad maxima de canicas en cada slot pero marque el 700 como limite espero ese valor sirva
def plot_distribution(distribution):
    max_cuenta = max(distribution)
    scale_factor = 700 / max_cuenta

    bars = [count * scale_factor for count in distribution]

    plt.bar(range(len(bars)), bars)
    plt.xlabel('DISTRIBUCION DE CANICAS')
    plt.ylabel('CANTIDAD DE CANICAS')
    plt.title(' DISTRIBUCION DE MAQUINA DE GALTON')
    plt.show()

if __name__ == "__principal__":
    num_bolas = 3000  # Número de bolas a dejar caer
    num_slots = 12    # Número de slots

    distribution = galton_machine(num_bolas, num_slots)
    plot_distribution(distribution)
