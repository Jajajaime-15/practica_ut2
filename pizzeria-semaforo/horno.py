from threading import Thread, Semaphore, Lock
import threading
import time
import random
from cocinero import *


class Horno:
    def __init__(self, cantidad):
        self.semaforo = Semaphore(cantidad)

    def hornear(self, pizza, cocinero):
        with self.semaforo:
            print(f" {cocinero} mete {pizza} al horno...")
            tiempo = random.randint(2, 5)
            time.sleep(tiempo)
            print(f"{pizza} lista (tardo {tiempo}s - por {cocinero})")
