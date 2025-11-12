import threading
from threading import Thread, Semaphore
from cocinero import Cocinero
from horno import Horno


def main():
    horno = Horno(2)  # 2 hornos disponibles
    cocineros = [
        Cocinero("Mario", horno),
        Cocinero("Luigi", horno),
        Cocinero("Peach", horno),
    ]
    for c in cocineros:
        c.start()
    for c in cocineros:
        c.join()


if __name__ == "__main__":
    main()
