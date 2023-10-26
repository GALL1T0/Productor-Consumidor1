import threading
import time
import random

class Estacionamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.autos = []
        self.mutex = threading.Lock()

    def agregar_auto(self):
        with self.mutex:
            if len(self.autos) < self.capacidad:
                self.autos.append(f'Auto-{len(self.autos) + 1}')
                print(f'Se añadió un auto. Total de autos: {len(self.autos)}')
            else:
                print('El estacionamiento está lleno. No se puede añadir más autos.')

    def retirar_auto(self):
        with self.mutex:
            if len(self.autos) > 0:
                auto = self.autos.pop()
                print(f'Se retiró un auto. Total de autos: {len(self.autos)}')
            else:
                print('El estacionamiento está vacío. No se puede retirar autos.')

def agregar_autos(estacionamiento):
    while True:
        tiempo_espera = random.choice([0.5, 1, 2])
        estacionamiento.agregar_auto()
        time.sleep(tiempo_espera)

def retirar_autos(estacionamiento):
    while True:
        tiempo_espera = random.choice([0.5, 1, 2])
        estacionamiento.retirar_auto()
        time.sleep(tiempo_espera)

if __name__ == "__main__":
    capacidad_estacionamiento = 12
    estacionamiento = Estacionamiento(capacidad_estacionamiento)

    hilo_agregar = threading.Thread(target=agregar_autos, args=(estacionamiento,))
    hilo_retirar = threading.Thread(target=retirar_autos, args=(estacionamiento,))

    hilo_agregar.start()
    hilo_retirar.start()

    while True:
        opcion = input("\nPulse 'q' para salir o 'f' para cambiar la frecuencia: ")
        if opcion == 'q':
            hilo_agregar.join()
            hilo_retirar.join()
            break
        elif opcion == 'f':
            nueva_frecuencia = input("Ingrese una nueva frecuencia (0.5, 1, o 2 segundos): ")
            if nueva_frecuencia in ['0.5', '1', '2']:
                hilo_agregar.join()
                hilo_retirar.join()
                hilo_agregar = threading.Thread(target=agregar_autos, args=(estacionamiento,))
                hilo_retirar = threading.Thread(target=retirar_autos, args=(estacionamiento,))
                hilo_agregar.start()
                hilo_retirar.start()
            else:
                print("Frecuencia no válida. Debe ser 0.5, 1 o 2 segundos.")
