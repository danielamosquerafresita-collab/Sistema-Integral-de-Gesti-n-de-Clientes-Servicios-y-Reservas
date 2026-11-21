
from abc import ABC, abstractmethod
from datetime import datetime


class Entidad(ABC):

    def __init__(self, identificador):
        if not identificador:
            raise ValueError("El identificador es obligatorio.")

        self.__identificador = identificador
        self.__fecha_creacion = datetime.now()

    @property
    def identificador(self):
        return self.__identificador

    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

    @abstractmethod
    def mostrar_informacion(self):
        pass
