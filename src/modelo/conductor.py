
from .errores import ReglaNegocioError
from .validaciones import texto_obligatorio


class Conductor:

    def __init__(
        self,
        nombre: str,
        rut: str,
        telefono: str,
        licencia: str,
        disponible: bool
    ):
        self._nombre = texto_obligatorio(nombre, "Nombre")
        self._rut = texto_obligatorio(rut, "RUT")
        self._telefono = texto_obligatorio(telefono, "Teléfono")
        self._licencia = texto_obligatorio(licencia, "Licencia")

        if sum(caracter.isdigit() for caracter in self._telefono) < 8:
            raise ReglaNegocioError(
                "El teléfono debe tener al menos 8 dígitos"
            )

        if not isinstance(disponible, bool):
            raise ReglaNegocioError(
                "La disponibilidad debe ser verdadera o falsa"
            )

        self._disponible = disponible

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def rut(self) -> str:
        return self._rut

    @property
    def telefono(self) -> str:
        return self._telefono

    @property
    def licencia(self) -> str:
        return self._licencia

    @property
    def disponible(self) -> bool:
        return self._disponible

    def consultarDisponibilidad(self) -> bool:
        return self._disponible

    def ocupar(self) -> None:
        if not self._disponible:
            raise ReglaNegocioError(
                "El conductor ya se encuentra ocupado"
            )

        self._disponible = False

    def disponibilizar(self) -> None:
        self._disponible = True
