from .vehiculo import Vehiculo
from .errores import ReglaNegocioError


class VehiculoRefrigerado(Vehiculo):

    def __init__(
        self,
        patente: str,
        marca: str,
        modelo: str,
        anio: int,
        disponible: bool,
        temperaturaMaxima: int
    ):
        super().__init__(
            patente,
            marca,
            modelo,
            anio,
            disponible
        )

        if not isinstance(temperaturaMaxima, int) or isinstance(temperaturaMaxima, bool):
            raise ReglaNegocioError(
                "La temperatura máxima debe ser un número entero"
            )

        self._temperaturaMaxima = temperaturaMaxima

    @property
    def temperaturaMaxima(self) -> int:
        return self._temperaturaMaxima

    @property
    def tipo(self) -> str:
        return "Vehículo refrigerado"
