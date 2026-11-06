from abc import ABC, abstractmethod

from .errores import ReglaNegocioError
from .validaciones import texto_obligatorio


class Vehiculo(ABC):

    def __init__(
        self,
        patente: str,
        marca: str,
        modelo: str,
        anio: int,
        disponible: bool
    ):
        self._patente = texto_obligatorio(patente, "Patente")
        self._marca = texto_obligatorio(marca, "Marca")
        self._modelo = texto_obligatorio(modelo, "Modelo")

        if not isinstance(anio, int) or isinstance(anio, bool):
            raise ReglaNegocioError(
                "El año debe ser un número entero"
            )

        if anio < 1900:
            raise ReglaNegocioError(
                "El año del vehículo no es válido"
            )

        if not isinstance(disponible, bool):
            raise ReglaNegocioError(
                "La disponibilidad debe ser verdadera o falsa"
            )

        self._anio = anio
        self._disponible = disponible

    @property
    def patente(self) -> str:
        return self._patente

    @property
    def marca(self) -> str:
        return self._marca

    @property
    def modelo(self) -> str:
        return self._modelo

    @property
    def anio(self) -> int:
        return self._anio

    @property
    def disponible(self) -> bool:
        return self._disponible

    def ocupar(self) -> None:
        if not self._disponible:
            raise ReglaNegocioError(
                "El vehículo ya se encuentra ocupado"
            )

        self._disponible = False

    def disponibilizar(self) -> None:
        self._disponible = True

    @property
    @abstractmethod
    def tipo(self) -> str:
        """Identifica el tipo de vehículo."""

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"{self._patente}, {self._marca}, {self._modelo})"
        )
