from .errores import ReglaNegocioError
from .validaciones import texto_obligatorio
from .pedido import Pedido
from .conductor import Conductor
from .vehiculo import Vehiculo


class Despacho:

    def __init__(
        self,
        id: str,
        pedido: Pedido,
        conductor: Conductor,
        vehiculo: Vehiculo
    ):
        self._id = texto_obligatorio(id, "Identificador")

        if not isinstance(pedido, Pedido):
            raise ReglaNegocioError(
                "El pedido debe ser una instancia de Pedido"
            )

        if not isinstance(conductor, Conductor):
            raise ReglaNegocioError(
                "El conductor debe ser una instancia de Conductor"
            )

        if not isinstance(vehiculo, Vehiculo):
            raise ReglaNegocioError(
                "El vehículo debe ser una instancia de Vehiculo"
            )

        if not conductor.disponible:
            raise ReglaNegocioError(
                "El conductor no está disponible"
            )

        if not vehiculo.disponible:
            raise ReglaNegocioError(
                "El vehículo no está disponible"
            )

        self._pedido = pedido
        self._conductor = conductor
        self._vehiculo = vehiculo
        self._estado = "Pendiente"

    @property
    def id(self) -> str:
        return self._id

    @property
    def pedido(self) -> Pedido:
        return self._pedido

    @property
    def conductor(self) -> Conductor:
        return self._conductor

    @property
    def vehiculo(self) -> Vehiculo:
        return self._vehiculo

    @property
    def estado(self) -> str:
        return self._estado

    def iniciar_despacho(self) -> None:
        if self._estado != "Pendiente":
            raise ReglaNegocioError(
                "El despacho no se encuentra pendiente"
            )

        self._conductor.ocupar()
        self._vehiculo.ocupar()
        self._estado = "En curso"

    def finalizar_despacho(self) -> None:
        if self._estado != "En curso":
            raise ReglaNegocioError(
                "El despacho no se encuentra en curso"
            )

        self._conductor.disponibilizar()
        self._vehiculo.disponibilizar()
        self._estado = "Finalizado"

    def __repr__(self) -> str:
        return (
            f"Despacho({self._id!r}, "
            f"estado={self._estado!r})"
        )
