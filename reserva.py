
from entidades import Entidad
from excepciones import (
    ReservaInvalidaError,
    OperacionNoPermitidaError
)


class Reserva(Entidad):

    ESTADOS = ("Pendiente", "Confirmada", "Cancelada")

    def __init__(self, identificador, cliente, servicio, duracion):
        super().__init__(identificador)

        from cliente import Cliente
        from servicios import Servicio

        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("Cliente inválido.")

        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("Servicio inválido.")

        servicio.validar_parametros(duracion)

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__costo = None

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self, descuento=0, impuesto=0):
        if self.__estado != "Pendiente":
            raise OperacionNoPermitidaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__costo = self.__servicio.calcular_costo(
            self.__duracion,
            descuento,
            impuesto
        )

        if self.__costo <= 0:
            raise ReservaInvalidaError("El costo calculado no es válido.")

        self.__estado = "Confirmada"
        return self.__costo

    def cancelar(self):
        if self.__estado == "Cancelada":
            raise OperacionNoPermitidaError(
                "La reserva ya está cancelada."
            )

        self.__estado = "Cancelada"
        return True

    def procesar(self):
        try:
            if self.__estado != "Confirmada":
                raise ReservaInvalidaError(
                    "La reserva debe estar confirmada."
                )

            return f"Reserva {self.identificador} procesada correctamente."

        except ReservaInvalidaError as error:
            raise ReservaInvalidaError(
                "No fue posible procesar la reserva."
            ) from error

    def mostrar_informacion(self):
        return (
            f"Reserva: {self.identificador}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.nombre}\n"
            f"Duración: {self.__duracion} horas\n"
            f"Estado: {self.__estado}\n"
            f"Costo: {self.__costo if self.__costo is not None else 'Pendiente'}"
        )
