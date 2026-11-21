
from abc import abstractmethod
from entidades import Entidad
from excepciones import DatosInvalidosError


class Servicio(Entidad):

    def __init__(self, identificador, nombre, tarifa_base):
        super().__init__(identificador)

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("Nombre de servicio inválido.")

        if isinstance(tarifa_base, bool) or not isinstance(tarifa_base, (int, float)):
            raise DatosInvalidosError("La tarifa debe ser numérica.")

        if tarifa_base <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")

        self._nombre = nombre.strip()
        self._tarifa_base = float(tarifa_base)

    @property
    def nombre(self):
        return self._nombre

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass

    @abstractmethod
    def mostrar_informacion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, identificador, tarifa_base, capacidad):
        super().__init__(
            identificador,
            "Reserva de sala",
            tarifa_base
        )

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise DatosInvalidosError("Capacidad de sala inválida.")

        self.__capacidad = capacidad

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("Duración de reserva inválida.")

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("Porcentajes inválidos.")

        subtotal = self.tarifa_base * duracion
        total = subtotal - (subtotal * descuento / 100)
        return round(total + total * impuesto / 100, 2)

    def mostrar_informacion(self):
        return (
            f"{self.nombre} | Tarifa por hora: "
            f"${self.tarifa_base:.2f} | Capacidad: {self.__capacidad}"
        )


class AlquilerEquipos(Servicio):

    def __init__(self, identificador, tarifa_base, tipo_equipo):
        super().__init__(
            identificador,
            "Alquiler de equipos",
            tarifa_base
        )

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise DatosInvalidosError("Tipo de equipo inválido.")

        self.__tipo_equipo = tipo_equipo.strip()

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("Duración de alquiler inválida.")

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("Porcentajes inválidos.")

        subtotal = self.tarifa_base * duracion
        total = subtotal - (subtotal * descuento / 100)
        return round(total + total * impuesto / 100, 2)

    def mostrar_informacion(self):
        return (
            f"{self.nombre} | Tarifa por hora: "
            f"${self.tarifa_base:.2f} | Equipo: {self.__tipo_equipo}"
        )


class AsesoriaEspecializada(Servicio):

    def __init__(self, identificador, tarifa_base, especialidad):
        super().__init__(
            identificador,
            "Asesoría especializada",
            tarifa_base
        )

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatosInvalidosError("Especialidad inválida.")

        self.__especialidad = especialidad.strip()

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise DatosInvalidosError("Duración de asesoría inválida.")

        return True

    def calcular_costo(self, duracion, descuento=0, impuesto=0):
        self.validar_parametros(duracion)

        if not 0 <= descuento <= 100 or not 0 <= impuesto <= 100:
            raise DatosInvalidosError("Porcentajes inválidos.")

        subtotal = self.tarifa_base * duracion
        total = subtotal - (subtotal * descuento / 100)
        return round(total + total * impuesto / 100, 2)

    def mostrar_informacion(self):
        return (
            f"{self.nombre} | Tarifa por hora: "
            f"${self.tarifa_base:.2f} | Especialidad: {self.__especialidad}"
        )
