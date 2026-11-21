
import re
from entidades import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)

        self.__nombre = self.validar_nombre(nombre)
        self.__correo = self.validar_correo(correo)
        self.__telefono = self.validar_telefono(telefono)

    @staticmethod
    def validar_nombre(nombre):
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del cliente es obligatorio."
            )

        if len(nombre.strip()) < 3:
            raise DatosInvalidosError(
                "El nombre debe tener mínimo 3 caracteres."
            )

        return nombre.strip().title()

    @staticmethod
    def validar_correo(correo):
        if not isinstance(correo, str):
            raise DatosInvalidosError("El correo no es válido.")

        patron = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"

        if not re.match(patron, correo):
            raise DatosInvalidosError(
                "El formato del correo electrónico es incorrecto."
            )

        return correo.lower().strip()

    @staticmethod
    def validar_telefono(telefono):
        telefono = str(telefono).strip()

        if not telefono.isdigit() or not (7 <= len(telefono) <= 15):
            raise DatosInvalidosError(
                "El teléfono debe contener entre 7 y 15 dígitos."
            )

        return telefono

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def mostrar_informacion(self):
        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
