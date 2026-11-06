from .errores import ReglaNegocioError
from .validaciones import texto_obligatorio


class Producto:
    def __init__(
        self, id, nombre, precio, cantidadDisponible,
        stockMinimo, peso, requiereRefrigeracion
    ):
        self._id = id
        self._nombre = nombre
        self._precio = precio
        self._cantidadDisponible = cantidadDisponible
        self._stockMinimo = stockMinimo
        self._peso = peso
        self._requiereRefrigeracion = requiereRefrigeracion

        if not isinstance(precio, int) or isinstance(precio, bool):
            raise ReglaNegocioError(
                "El precio debe ser un número entero"
            )

        if precio < 1:
            raise ReglaNegocioError(
                "El precio debe ser mayor que cero"
            )

        if not isinstance(cantidadDisponible, int) or isinstance(cantidadDisponible, bool):
            raise ReglaNegocioError(
                "La cantidad disponible debe ser un número entero"
            )

        if cantidadDisponible < 0:
            raise ReglaNegocioError(
                "La cantidad disponible no puede ser negativa"
            )

        if not isinstance(stockMinimo, int) or isinstance(stockMinimo, bool):
            raise ReglaNegocioError(
                "El stock mínimo debe ser un número entero"
            )

        if stockMinimo < 0:
            raise ReglaNegocioError(
                "El stock mínimo no puede ser negativo"
            )

        if not isinstance(peso, (int, float)) or isinstance(peso, bool):
            raise ReglaNegocioError(
                "El peso debe ser un número"
            )

        if peso <= 0:
            raise ReglaNegocioError(
                "El peso debe ser mayor que cero"
            )

        if not isinstance(requiereRefrigeracion, bool):
            raise ReglaNegocioError(
                "La refrigeración debe ser True o False"
            )

        self._precio = precio
        self._cantidadDisponible = cantidadDisponible
        self._stockMinimo = stockMinimo
        self._peso = peso
        self._requiereRefrigeracion = requiereRefrigeracion
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def cantidadDisponible(self):
        return self._cantidadDisponible

    @property
    def stockMinimo(self):
        return self._stockMinimo

    @property
    def peso(self):
        return self._peso

    @property
    def requiereRefrigeracion(self):
        return self._requiereRefrigeracion