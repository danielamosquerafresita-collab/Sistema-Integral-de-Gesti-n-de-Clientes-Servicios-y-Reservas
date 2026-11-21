
class ErrorSistema(Exception):
    """Excepción base del sistema Software FJ."""
    pass


class DatosInvalidosError(ErrorSistema):
    """Se genera cuando los datos ingresados son incorrectos."""
    pass


class ClienteExistenteError(ErrorSistema):
    """Se genera cuando un cliente ya está registrado."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una reserva no cumple las condiciones."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se genera cuando se intenta realizar una operación prohibida."""
    pass


class RecursoNoEncontradoError(ErrorSistema):
    """Se genera cuando no se encuentra un elemento."""
    pass
