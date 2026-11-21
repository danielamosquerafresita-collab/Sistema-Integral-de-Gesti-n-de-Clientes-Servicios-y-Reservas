
import logging

from cliente import Cliente
from servicios import (
    ReservaSala,
    AlquilerEquipos,
    AsesoriaEspecializada
)
from gestor import GestorSistema


# Crear administrador del sistema
sistema = GestorSistema()


# Función para ejecutar operaciones sin detener el programa
def ejecutar(titulo, operacion):

    print(f"\n--- {titulo} ---")

    try:
        resultado = operacion()

    except Exception as error:
        logging.exception("Error en operación: %s", titulo)
        print("ERROR CONTROLADO:", error)
        return None

    else:
        print("Operación realizada correctamente.")

        if resultado is not None:
            print(resultado)

        return resultado

    finally:
        print("Operación finalizada.")


def iniciar_sistema():

    print("\n")
    print("=" * 50)
    print("       SOFTWARE FJ")
    print(" SISTEMA DE GESTIÓN INTEGRAL")
    print("=" * 50)

    # OPERACIÓN 1: Registrar primer cliente
    cliente1 = Cliente(
        "C001",
        "Daniela Mosquera",
        "daniela@gmail.com",
        "3001234567"
    )

    ejecutar(
        "1. Registrar cliente",
        lambda: sistema.registrar_cliente(cliente1)
    )

    # OPERACIÓN 2: Registrar segundo cliente
    cliente2 = Cliente(
        "C002",
        "Andres Martinez",
        "andres@gmail.com",
        "3101234567"
    )

    ejecutar(
        "2. Registrar segundo cliente",
        lambda: sistema.registrar_cliente(cliente2)
    )

    # OPERACIÓN 3: Intentar registrar cliente inválido
    ejecutar(
        "3. Registrar cliente con correo incorrecto",
        lambda: Cliente(
            "C003",
            "Carlos Perez",
            "correo_incorrecto",
            "3201234567"
        )
    )

    # OPERACIÓN 4: Intentar registrar cliente duplicado
    ejecutar(
        "4. Registrar cliente duplicado",
        lambda: sistema.registrar_cliente(cliente1)
    )

    # OPERACIÓN 5: Crear servicio de salas
    sala = ReservaSala(
        "S001",
        50000,
        20
    )

    ejecutar(
        "5. Registrar servicio de salas",
        lambda: sistema.registrar_servicio(sala)
    )

    # OPERACIÓN 6: Crear servicio de equipos
    equipo = AlquilerEquipos(
        "S002",
        30000,
        "Computador portátil"
    )

    ejecutar(
        "6. Registrar alquiler de equipos",
        lambda: sistema.registrar_servicio(equipo)
    )

    # OPERACIÓN 7: Crear servicio de asesoría
    asesoria = AsesoriaEspecializada(
        "S003",
        80000,
        "Desarrollo de software"
    )

    ejecutar(
        "7. Registrar asesoría especializada",
        lambda: sistema.registrar_servicio(asesoria)
    )

    # OPERACIÓN 8: Crear servicio inválido
    ejecutar(
        "8. Intentar crear servicio con tarifa negativa",
        lambda: ReservaSala("S004", -5000, 15)
    )

    # OPERACIÓN 9: Crear reserva correctamente
    reserva1 = ejecutar(
        "9. Crear reserva de sala",
        lambda: sistema.crear_reserva(
            "R001", "C001", "S001", 3
        )
    )

    # OPERACIÓN 10: Crear reserva con cliente inexistente
    ejecutar(
        "10. Intentar reservar con cliente inexistente",
        lambda: sistema.crear_reserva(
            "R002", "C999", "S001", 2
        )
    )

    # OPERACIÓN 11: Crear reserva con servicio inexistente
    ejecutar(
        "11. Intentar reservar servicio inexistente",
        lambda: sistema.crear_reserva(
            "R003", "C001", "S999", 2
        )
    )

    # OPERACIÓN 12: Confirmar reserva
    if reserva1:
        ejecutar(
            "12. Confirmar reserva con descuento e impuesto",
            lambda: sistema.confirmar_reserva(
                "R001", 10, 19
            )
        )

        # OPERACIÓN 13: Procesar reserva
        ejecutar(
            "13. Procesar reserva confirmada",
            reserva1.procesar
        )

    # OPERACIÓN 14: Cancelar reserva
    if reserva1:
        ejecutar(
            "14. Cancelar reserva",
            lambda: sistema.cancelar_reserva("R001")
        )

    # OPERACIÓN 15: Intentar confirmar reserva cancelada
    ejecutar(
        "15. Confirmar reserva cancelada",
        lambda: sistema.confirmar_reserva("R001")
    )

    # OPERACIÓN 16: Mostrar información
    print("\n========== CLIENTES ==========")

    for cliente in sistema.listar_clientes():
        print(cliente.mostrar_informacion())
        print("------------------------------")

    print("\n========== SERVICIOS ==========")

    for servicio in sistema.listar_servicios():
        print(servicio.mostrar_informacion())
        print("------------------------------")

    print("\n========== RESERVAS ==========")

    for reserva in sistema.listar_reservas():
        print(reserva.mostrar_informacion())
        print("------------------------------")

    # Resumen general
    sistema.mostrar_resumen()

    print("\nSistema ejecutado correctamente.")
    print("Los eventos y errores están en logs/sistema.log")


if __name__ == "__main__":
    iniciar_sistema()
