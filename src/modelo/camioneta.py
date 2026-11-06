from .vehiculo import Vehiculo
from .errores import ReglaNegocioError


class Camioneta(Vehiculo):

    def __init__(
        self,
        patente: str,
        marca: str,
        modelo: str,
        anio: int,
        disponible: bool,
        capacidadCarga: int
    ):
        super().__init__(
            patente,
            marca,
            modelo,
            anio,
            disponible
        )

        if not isinstance(capacidadCarga, int) or isinstance(capacidadCarga, bool):
            raise ReglaNegocioError(
                "La capacidad de carga debe ser un número entero"
            )

        if capacidadCarga <= 0:
            raise ReglaNegocioError(
                "La capacidad de carga debe ser mayor que cero"
            )

        self._capacidadCarga = capacidadCarga

    @property
    def capacidadCarga(self) -> int:
        return self._capacidadCarga

    @property
    def tipo(self) -> str:
        return "Camioneta"
