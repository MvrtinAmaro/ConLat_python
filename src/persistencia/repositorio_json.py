import json
from pathlib import Path


class RepositorioJSON:

    def __init__(self, nombre_archivo):

        ruta_proyecto = Path(__file__).resolve().parent.parent
        self.carpeta_data = ruta_proyecto / "data"

        self.carpeta_data.mkdir(exist_ok=True)

        self.ruta_archivo = self.carpeta_data / nombre_archivo

        if not self.ruta_archivo.exists():
            self.guardar([])

    def cargar(self):

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                return json.load(archivo)

        except (json.JSONDecodeError, OSError):
            return []

    def guardar(self, datos):

        with open(self.ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
