# Importamos la librería re para trabajar con expresiones regulares
# y validar el formato del correo electrónico.
import re

# Importamos la clase Entidad, de la cual heredará Cliente.
from entidades import Entidad

# Importamos la excepción personalizada para controlar datos incorrectos.
from excepciones import DatosInvalidosError


# Creamos la clase Cliente, que hereda de la clase Entidad.
class Cliente(Entidad):

    # Constructor: recibe los datos necesarios para crear un cliente.
    def __init__(self, identificador, nombre, correo, telefono):

        # Llamamos al constructor de la clase padre para inicializar el ID.
        super().__init__(identificador)

        # Validamos el nombre y lo guardamos como atributo privado.
        self.__nombre = self.validar_nombre(nombre)

        # Validamos el correo y lo guardamos como atributo privado.
        self.__correo = self.validar_correo(correo)

        # Validamos el teléfono y lo guardamos como atributo privado.
        self.__telefono = self.validar_telefono(telefono)

    # Método estático para validar el nombre del cliente.
    @staticmethod
    def validar_nombre(nombre):

        # Comprobamos que el nombre sea texto y no esté vacío.
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError(
                "El nombre del cliente es obligatorio."
            )

        # Verificamos que el nombre tenga mínimo tres caracteres.
        if len(nombre.strip()) < 3:
            raise DatosInvalidosError(
                "El nombre debe tener mínimo 3 caracteres."
            )

        # Eliminamos espacios innecesarios y ponemos
        # la primera letra de cada palabra en mayúscula.
        return nombre.strip().title()

    # Método estático para validar el correo electrónico.
    @staticmethod
    def validar_correo(correo):

        # Verificamos que el correo sea una cadena de texto.
        if not isinstance(correo, str):
            raise DatosInvalidosError("El correo no es válido.")

        # Expresión regular que comprueba la estructura del correo.
        patron = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"

        # Si el correo no coincide con el patrón, generamos una excepción.
        if not re.match(patron, correo):
            raise DatosInvalidosError(
                "El formato del correo electrónico es incorrecto."
            )

        # Convertimos el correo a minúsculas y eliminamos espacios.
        return correo.lower().strip()

    # Método estático para validar el número de teléfono.
    @staticmethod
    def validar_telefono(telefono):

        # Convertimos el teléfono a texto y eliminamos espacios.
        telefono = str(telefono).strip()

        # Verificamos que contenga únicamente números
        # y que tenga entre 7 y 15 dígitos.
        if not telefono.isdigit() or not (7 <= len(telefono) <= 15):
            raise DatosInvalidosError(
                "El teléfono debe contener entre 7 y 15 dígitos."
            )

        # Retornamos el teléfono si cumple las condiciones.
        return telefono

    # Propiedad para consultar el nombre sin acceder directamente
    # al atributo privado.
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para consultar el correo electrónico.
    @property
    def correo(self):
        return self.__correo

    # Propiedad para consultar el teléfono.
    @property
    def telefono(self):
        return self.__telefono

    # Método que organiza y devuelve la información completa del cliente.
    def mostrar_informacion(self):
        return (
            f"ID: {self.identificador}\n"
            f"Nombre: {self.nombre}\n"
            f"Correo: {self.correo}\n"
            f"Teléfono: {self.telefono}"
        )

    # Método especial que define cómo se representa el cliente
    # cuando se utiliza print() sobre un objeto Cliente.
    def __str__(self):
        return f"{self.nombre} - {self.correo}"