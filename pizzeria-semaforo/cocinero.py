from threading import Thread, Semaphore, Lock
import threading
import time
import random
from horno import *


class Cocinero(Thread):
    def __init__(self, nombre, horno):
        super().__init__()
        self.nombre = nombre
        self.horno = horno

    def run(self):
        for i in range(3):  # 3 pizzas por cocinero
            pizza = f"Pizza {i+1} de {self.nombre}"
            self.horno.hornear(pizza, self.nombre)
            time.sleep(random.uniform(0.5, 1.5))
        print(f"{self.nombre} ha terminado sus pizzas \n")
