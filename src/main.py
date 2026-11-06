
from interfaz.ventana_principal import VentanaPrincipal

from persistencia.repositorio_json import RepositorioJSON

from modelo.cliente import Cliente
from modelo.producto import Producto


def main():

    # Crear repositorios
    repo_clientes = RepositorioJSON("clientes.json")
    repo_productos = RepositorioJSON("productos.json")

    # Recuperar clientes
    datos_clientes = repo_clientes.cargar()

    clientes = [
        Cliente(
            dato["rut"],
            dato["nombre"],
            dato["direccion"],
            dato["correo"],
            dato["telefono"]
        )
        for dato in datos_clientes
    ]

    # Recuperar productos
    datos_productos = repo_productos.cargar()

    productos = [
        Producto(
            dato["id"],
            dato["nombre"],
            dato["precio"],
            dato["cantidadDisponible"],
            dato["stockMinimo"],
            dato.get("peso", 0.5),
            dato.get("requiereRefrigeracion", False)
        )
        for dato in datos_productos
    ]

    # Inicializar las demás listas
    pedidos = []
    conductores = []
    vehiculos = []
    despachos = []

    aplicacion = VentanaPrincipal(
        clientes,
        productos,
        pedidos,
        conductores,
        vehiculos,
        despachos
    )

    aplicacion.iniciar()


if __name__ == "__main__":
    main()
