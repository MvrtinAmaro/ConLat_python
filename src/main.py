
from interfaz.ventana_principal import VentanaPrincipal

from persistencia.repositorio_json import RepositorioJSON

from modelo.cliente import Cliente
from modelo.producto import Producto
from modelo.pedido import Pedido
from modelo.detalle_pedido import DetallePedido
from modelo.conductor import Conductor
from modelo.camioneta import Camioneta
from modelo.vehiculo_refrigerado import VehiculoRefrigerado
from modelo.despacho import Despacho


def main():

    repo_clientes = RepositorioJSON("clientes.json")
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


    repo_productos = RepositorioJSON("productos.json")
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



    repo_pedidos = RepositorioJSON("pedidos.json")
    datos_pedidos = repo_pedidos.cargar()

    pedidos = []

    for dato in datos_pedidos:

        cliente = next(
            (c for c in clientes if c.rut == dato["rut_cliente"]),
            None
        )

        if cliente is None:
            continue

        pedido = Pedido(dato["id"], cliente)

        for detalle in dato["detalles"]:

            producto = next(
                (p for p in productos if p.id == detalle["id_producto"]),
                None
            )

            if producto is not None:
                pedido.agregar_detalle(
                    DetallePedido(producto, detalle["cantidad"])
                )

        pedido.cambiar_estado(dato.get("estado", "Pendiente"))
        pedidos.append(pedido)


    repo_conductores = RepositorioJSON("conductores.json")
    datos_conductores = repo_conductores.cargar()

    conductores = [
        Conductor(
            dato["nombre"],
            dato["rut"],
            dato["telefono"],
            dato["licencia"],
            dato.get("disponible", True)
        )
        for dato in datos_conductores
    ]

    repo_vehiculos = RepositorioJSON("vehiculos.json")
    datos_vehiculos = repo_vehiculos.cargar()

    vehiculos = []

    for dato in datos_vehiculos:

        if dato["tipo"] == "Camioneta":
            vehiculo = Camioneta(
                dato["patente"],
                dato["marca"],
                dato["modelo"],
                dato["anio"],
                dato.get("disponible", True),
                dato["capacidadCarga"]
            )

        elif dato["tipo"] in ("Vehículo refrigerado", "Refrigerado"):
            vehiculo = VehiculoRefrigerado(
                dato["patente"],
                dato["marca"],
                dato["modelo"],
                dato["anio"],
                dato.get("disponible", True),
                dato["temperaturaMaxima"]
            )

        else:
            continue

        vehiculos.append(vehiculo)


    repo_despachos = RepositorioJSON("despachos.json")
    datos_despachos = repo_despachos.cargar()

    despachos = []

    for dato in datos_despachos:

        pedido = next(
            (p for p in pedidos if p.id == dato["id_pedido"]),
            None
        )

        conductor = next(
            (c for c in conductores if c.rut == dato["rut_conductor"]),
            None
        )

        vehiculo = next(
            (v for v in vehiculos if v.patente == dato["patente"]),
            None
        )

        if pedido is None or conductor is None or vehiculo is None:
            continue

        despacho = Despacho(dato["id"], pedido, conductor, vehiculo)

        estado = dato.get("estado", "Pendiente")

        if estado in ("En curso", "Finalizado"):
            despacho.iniciar_despacho()

        if estado == "Finalizado":
            despacho.finalizar_despacho()

        despachos.append(despacho)

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
