from .errores import ReglaNegocioError
from .validaciones import texto_obligatorio

class Cliente:
    def __init__(self, rut: str, nombre: str, direccion: str, correo: str, telefono: str):
        self._rut = texto_obligatorio(rut, "Rut")
        self._nombre = texto_obligatorio(nombre, "Nombre")
        self._direccion = texto_obligatorio(direccion, "Direccion")
        self._correo = texto_obligatorio(correo, "Correo")
        self._telefono = texto_obligatorio(telefono, "Telefono")

        if sum(caracter.isdigit() for caracter in self._telefono) < 8:
            raise ReglaNegocioError(
            "El teléfono debe tener al menos 8 dígitos"
        )

    @property
    def rut(self) -> str:
        return self._rut

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def direccion(self) -> str:
        return self._direccion

    @property
    def telefono(self) -> str:
        return self._telefono

    @property
    def correo(self) -> str:
        return self._correo

    