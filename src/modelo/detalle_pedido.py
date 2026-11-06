
from .errores import ReglaNegocioError
from .producto import Producto


class DetallePedido:

    def __init__(
        self,
        producto: Producto,
        cantidad: int
    ):
        if not isinstance(producto, Producto):
            raise ReglaNegocioError(
                "El producto debe ser una instancia de Producto"
            )

        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            raise ReglaNegocioError(
                "La cantidad debe ser un número entero"
            )

        if cantidad < 1:
            raise ReglaNegocioError(
                "La cantidad debe ser mayor que cero"
            )

        if cantidad > producto.cantidadDisponible:
            raise ReglaNegocioError(
                "No existe suficiente stock del producto"
            )

        self._producto = producto
        self._cantidad = cantidad
        self._precioUnitario = producto.precio

    @property
    def producto(self) -> Producto:
        return self._producto

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @property
    def precioUnitario(self) -> int:
        return self._precioUnitario

    @property
    def subtotal(self) -> int:
        return self._precioUnitario * self._cantidad
