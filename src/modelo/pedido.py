from .errores import ReglaNegocioError
from .validaciones import texto_obligatorio
from .cliente import Cliente
from .detalle_pedido import DetallePedido


class Pedido:

    def __init__(
        self,
        id: str,
        cliente: Cliente
    ):
        self._id = texto_obligatorio(id, "Identificador")

        if not isinstance(cliente, Cliente):
            raise ReglaNegocioError(
                "El cliente debe ser una instancia de Cliente"
            )

        self._cliente = cliente
        self._detalles = []
        self._estado = "Pendiente"

    @property
    def id(self) -> str:
        return self._id

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @property
    def detalles(self) -> tuple:
        return tuple(self._detalles)

    @property
    def estado(self) -> str:
        return self._estado

    @property
    def total(self) -> int:
        return sum(
            detalle.subtotal for detalle in self._detalles
        )

    def agregar_detalle(self, detalle: DetallePedido) -> None:
        if not isinstance(detalle, DetallePedido):
            raise ReglaNegocioError(
                "El detalle debe ser una instancia de DetallePedido"
            )

        self._detalles.append(detalle)

    def cambiar_estado(self, nuevo_estado: str) -> None:
        estado = texto_obligatorio(nuevo_estado, "Estado")

        estados_validos = [
            "Pendiente",
            "Confirmado",
            "En preparación",
            "Enviado",
            "Entregado",
            "Cancelado"
        ]

        if estado not in estados_validos:
            raise ReglaNegocioError(
                "El estado del pedido no es válido"
            )

        self._estado = estado

    def __repr__(self) -> str:
        return (
            f"Pedido({self._id!r}, "
            f"cliente={self._cliente.nombre!r}, "
            f"total={self.total})"
        )
