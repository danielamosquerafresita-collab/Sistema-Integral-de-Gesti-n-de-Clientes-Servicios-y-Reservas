
import logging
import os

from cliente import Cliente
from servicios import Servicio
from reserva import Reserva

from excepciones import (
    ClienteExistenteError,
    RecursoNoEncontradoError,
    ServicioNoDisponibleError,
    DatosInvalidosError
)


# Crear carpeta de registros automáticamente
os.makedirs("logs", exist_ok=True)


# Configuración del sistema de logs
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


class GestorSistema:

    def __init__(self):
        self.__clientes = []
        self.__servicios = []
        self.__reservas = []

        logging.info("Sistema Software FJ iniciado.")

    def registrar_cliente(self, cliente):

        try:
            if not isinstance(cliente, Cliente):
                raise DatosInvalidosError("El objeto no es un cliente válido.")

            if any(c.identificador == cliente.identificador
                   for c in self.__clientes):
                raise ClienteExistenteError(
                    "El cliente ya está registrado."
                )

            self.__clientes.append(cliente)

        except Exception:
            logging.exception("Error al registrar cliente.")
            raise

        else:
            logging.info(
                "Cliente registrado: %s", cliente.identificador
            )

        finally:
            logging.info("Finalizó operación de registro de cliente.")

        return True

    def registrar_servicio(self, servicio):

        try:
            if not isinstance(servicio, Servicio):
                raise DatosInvalidosError("Servicio inválido.")

            if any(s.identificador == servicio.identificador
                   for s in self.__servicios):
                raise DatosInvalidosError(
                    "El servicio ya está registrado."
                )

            self.__servicios.append(servicio)

        except Exception:
            logging.exception("Error al registrar servicio.")
            raise

        else:
            logging.info(
                "Servicio registrado: %s", servicio.identificador
            )

        finally:
            logging.info("Finalizó operación de registro de servicio.")

        return True

    def crear_reserva(self, identificador, id_cliente,
                      id_servicio, duracion):

        try:
            cliente = next(
                (c for c in self.__clientes
                 if c.identificador == id_cliente),
                None
            )

            servicio = next(
                (s for s in self.__servicios
                 if s.identificador == id_servicio),
                None
            )

            if cliente is None:
                raise RecursoNoEncontradoError(
                    "No se encontró el cliente."
                )

            if servicio is None:
                raise ServicioNoDisponibleError(
                    "El servicio no está registrado o disponible."
                )

            if any(r.identificador == identificador
                   for r in self.__reservas):
                raise DatosInvalidosError(
                    "El identificador de reserva ya existe."
                )

            reserva = Reserva(
                identificador,
                cliente,
                servicio,
                duracion
            )

            self.__reservas.append(reserva)

        except Exception:
            logging.exception("Error al crear reserva.")
            raise

        else:
            logging.info("Reserva creada: %s", identificador)

        finally:
            logging.info("Finalizó operación de creación de reserva.")

        return reserva

    def confirmar_reserva(self, identificador,
                          descuento=0, impuesto=0):

        try:
            reserva = self.buscar_reserva(identificador)

            costo = reserva.confirmar(descuento, impuesto)

        except Exception:
            logging.exception("Error al confirmar reserva.")
            raise

        else:
            logging.info("Reserva confirmada: %s", identificador)
            return costo

        finally:
            logging.info("Finalizó operación de confirmación.")

    def cancelar_reserva(self, identificador):

        try:
            reserva = self.buscar_reserva(identificador)
            reserva.cancelar()

        except Exception:
            logging.exception("Error al cancelar reserva.")
            raise

        else:
            logging.info("Reserva cancelada: %s", identificador)
            return True

        finally:
            logging.info("Finalizó operación de cancelación.")

    def buscar_reserva(self, identificador):

        reserva = next(
            (r for r in self.__reservas
             if r.identificador == identificador),
            None
        )

        if reserva is None:
            raise RecursoNoEncontradoError(
                "Reserva no encontrada."
            )

        return reserva

    def listar_clientes(self):
        return list(self.__clientes)

    def listar_servicios(self):
        return list(self.__servicios)

    def listar_reservas(self):
        return list(self.__reservas)

    def mostrar_resumen(self):

        print("\n========== RESUMEN SOFTWARE FJ ==========")

        print("Clientes registrados:", len(self.__clientes))
        print("Servicios registrados:", len(self.__servicios))
        print("Reservas registradas:", len(self.__reservas))

        print("=========================================")

        logging.info("Consulta del resumen del sistema.")
