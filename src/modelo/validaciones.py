
from .errores import ReglaNegocioError


def texto_obligatorio(valor, nombre_campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ReglaNegocioError(
            f"{nombre_campo} es obligatorio"
        )

    return valor.strip()
