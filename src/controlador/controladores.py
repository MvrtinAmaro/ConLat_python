
from tkinter import messagebox

from modelo.cliente import Cliente
from modelo.producto import Producto
from modelo.pedido import Pedido
from modelo.detalle_pedido import DetallePedido
from modelo.despacho import Despacho
from modelo.errores import ReglaNegocioError
from persistencia.repositorio_json import RepositorioJSON


class ControladorClientes:

    def __init__(self, vista, clientes):
        self.vista = vista
        self.clientes = clientes

        self.repositorio = RepositorioJSON("clientes.json")

        self.vista.boton_registrar.config(
            command=self.registrar_cliente
        )

        self.cargar_clientes()

    def cargar_clientes(self):

        for cliente in self.clientes:
            self.vista.tabla.insert(
                "",
                "end",
                values=(
                    cliente.rut,
                    cliente.nombre,
                    cliente.direccion,
                    cliente.correo,
                    cliente.telefono
                )
            )

    def registrar_cliente(self):

        try:
            rut = self.vista.entradas["RUT"].get()
            nombre = self.vista.entradas["Nombre"].get()
            direccion = self.vista.entradas["Direccion"].get()
            correo = self.vista.entradas["Correo"].get()
            telefono = self.vista.entradas["Telefono"].get()

            cliente = Cliente(
                rut, nombre, direccion, correo, telefono
            )

            for existente in self.clientes:
                if existente.rut == cliente.rut:
                    raise ReglaNegocioError("El cliente ya existe")

            self.clientes.append(cliente)

            self.repositorio.guardar([
                {
                    "rut": c.rut,
                    "nombre": c.nombre,
                    "direccion": c.direccion,
                    "correo": c.correo,
                    "telefono": c.telefono
                }
                for c in self.clientes
            ])

            self.vista.tabla.insert(
                "",
                "end",
                values=(
                    cliente.rut,
                    cliente.nombre,
                    cliente.direccion,
                    cliente.correo,
                    cliente.telefono
                )
            )

            self.limpiar_formulario()

        except ReglaNegocioError as error:
            messagebox.showerror("Error", str(error))

    def limpiar_formulario(self):

        for entrada in self.vista.entradas.values():
            entrada.delete(0, "end")


class ControladorInventario:

    def __init__(self, vista, productos):
        self.vista = vista
        self.productos = productos

        self.repositorio = RepositorioJSON("productos.json")

        self.vista.boton_registrar.config(
            command=self.registrar_producto
        )

        self.cargar_productos()

    def cargar_productos(self):

        for producto in self.productos:
            self.vista.tabla.insert(
                "",
                "end",
                values=(
                    producto.id,
                    producto.nombre,
                    producto.precio,
                    producto.cantidadDisponible,
                    producto.stockMinimo,
                    producto.peso,
                    "Sí" if producto.requiereRefrigeracion else "No"
                )
            )

    def registrar_producto(self):

        try:
            id_producto = self.vista.entradas["ID"].get()
            nombre = self.vista.entradas["Nombre"].get()
            precio = int(self.vista.entradas["Precio"].get())

            cantidad = int(
                self.vista.entradas["Cantidad disponible"].get()
            )

            stock_minimo = int(
                self.vista.entradas["Stock minimo"].get()
            )

            peso = float(
                self.vista.entradas["Peso por unidad (kg)"].get()
            )

            refrigeracion = self.vista.refrigeracion.get()

            producto = Producto(
                id_producto,
                nombre,
                precio,
                cantidad,
                stock_minimo,
                peso,
                refrigeracion
            )

            for existente in self.productos:
                if existente.id == producto.id:
                    raise ReglaNegocioError("El producto ya existe")

            self.productos.append(producto)

            self.repositorio.guardar([
                {
                    "id": p.id,
                    "nombre": p.nombre,
                    "precio": p.precio,
                    "cantidadDisponible": p.cantidadDisponible,
                    "stockMinimo": p.stockMinimo,
                    "peso": p.peso,
                    "requiereRefrigeracion": p.requiereRefrigeracion
                }
                for p in self.productos
            ])

            self.vista.tabla.insert(
                "",
                "end",
                values=(
                    producto.id,
                    producto.nombre,
                    producto.precio,
                    producto.cantidadDisponible,
                    producto.stockMinimo,
                    producto.peso,
                    "Sí" if producto.requiereRefrigeracion else "No"
                )
            )

            self.limpiar_formulario()

        except ValueError:
            messagebox.showerror(
                "Error",
                "Ingrese valores numericos validos"
            )

        except ReglaNegocioError as error:
            messagebox.showerror("Error", str(error))

    def limpiar_formulario(self):

        for entrada in self.vista.entradas.values():
            entrada.delete(0, "end")

        self.vista.refrigeracion.set(False)




class ControladorPedidos:

    def __init__(self, vista, clientes, productos, pedidos):
        self.vista = vista
        self.clientes = clientes
        self.productos = productos
        self.pedidos = pedidos
        self.detalles = []

        self.repositorio = RepositorioJSON("pedidos.json")

        self.actualizar_clientes()
        self.actualizar_productos()
        self.cargar_pedidos()

        self.vista.boton_agregar.config(
            command=self.agregar_producto
        )

        self.vista.boton_crear.config(
            command=self.crear_pedido
        )

    def cargar_pedidos(self):
        for pedido in self.pedidos:
            self.insertar_pedido_en_tabla(pedido)

    def insertar_pedido_en_tabla(self, pedido):
        self.vista.tabla_pedidos.insert(
            "",
            "end",
            values=(
                pedido.id,
                pedido.cliente.nombre,
                len(pedido.detalles),
                pedido.total,
                pedido.estado
            )
        )

    def actualizar_clientes(self):
        self.vista.cliente["values"] = [
            cliente.nombre for cliente in self.clientes
        ]

    def actualizar_productos(self):
        self.vista.producto["values"] = [
            producto.nombre for producto in self.productos
        ]

    def agregar_producto(self):
        try:
            nombre_producto = self.vista.producto.get()
            cantidad = int(self.vista.cantidad.get())

            producto = next(
                (p for p in self.productos
                 if p.nombre == nombre_producto),
                None
            )

            if producto is None:
                raise ReglaNegocioError("Seleccione un producto")

            detalle = DetallePedido(producto, cantidad)
            self.detalles.append(detalle)

            self.vista.tabla.insert(
                "",
                "end",
                values=(
                    producto.nombre,
                    detalle.cantidad,
                    detalle.precioUnitario,
                    detalle.subtotal
                )
            )

            self.actualizar_total()
            self.vista.cantidad.delete(0, "end")

        except ValueError:
            messagebox.showerror(
                "Error",
                "La cantidad debe ser un número entero"
            )

        except ReglaNegocioError as error:
            messagebox.showerror("Error", str(error))

    def actualizar_total(self):
        total = sum(
            detalle.subtotal for detalle in self.detalles
        )

        self.vista.total.config(
            text=f"Total del pedido: ${total}"
        )

    def crear_pedido(self):
        try:
            nombre_cliente = self.vista.cliente.get()

            cliente = next(
                (c for c in self.clientes
                 if c.nombre == nombre_cliente),
                None
            )

            if cliente is None:
                raise ReglaNegocioError("Seleccione un cliente")

            if not self.detalles:
                raise ReglaNegocioError(
                    "El pedido debe contener productos"
                )

            id_pedido = f"PED-{len(self.pedidos) + 1}"

            pedido = Pedido(id_pedido, cliente)

            for detalle in self.detalles:
                pedido.agregar_detalle(detalle)

            self.pedidos.append(pedido)

            # Guardar pedidos en JSON
            datos_pedidos = []

            for p in self.pedidos:
                datos_pedidos.append({
                    "id": p.id,
                    "rut_cliente": p.cliente.rut,
                    "estado": p.estado,
                    "detalles": [
                        {
                            "id_producto": d.producto.id,
                            "cantidad": d.cantidad
                        }
                        for d in p.detalles
                    ]
                })

            self.repositorio.guardar(datos_pedidos)

            self.insertar_pedido_en_tabla(pedido)

            messagebox.showinfo(
                "Pedido creado",
                f"Se creó correctamente el pedido {id_pedido}"
            )

            self.limpiar_pedido()

        except ReglaNegocioError as error:
            messagebox.showerror("Error", str(error))

    def limpiar_pedido(self):
        self.detalles.clear()

        for elemento in self.vista.tabla.get_children():
            self.vista.tabla.delete(elemento)

        self.vista.total.config(
            text="Total del pedido: $0"
        )



class ControladorDespachos:

    def __init__(self, vista, pedidos, conductores, vehiculos, despachos):
        self.vista = vista
        self.pedidos = pedidos
        self.conductores = conductores
        self.vehiculos = vehiculos
        self.despachos = despachos

        self.repositorio = RepositorioJSON("despachos.json")

        self.actualizar_pedidos()
        self.actualizar_conductores()
        self.actualizar_vehiculos()
        self.cargar_despachos()

        self.vista.boton_asignar.config(
            command=self.asignar_despacho
        )

    def cargar_despachos(self):
        for despacho in self.despachos:
            self.insertar_despacho_en_tabla(despacho)

    def insertar_despacho_en_tabla(self, despacho):
        self.vista.tabla.insert(
            "",
            "end",
            values=(
                despacho.id,
                despacho.pedido.id,
                despacho.conductor.nombre,
                despacho.vehiculo.patente,
                despacho.estado
            )
        )

    def guardar_despachos(self):
        self.repositorio.guardar([
            {
                "id": d.id,
                "id_pedido": d.pedido.id,
                "rut_conductor": d.conductor.rut,
                "patente": d.vehiculo.patente,
                "estado": d.estado
            }
            for d in self.despachos
        ])

    def actualizar_pedidos(self):
        # Solo los pedidos que todavia no tienen un despacho asignado
        con_despacho = {d.pedido.id for d in self.despachos}

        self.vista.selecciones["Pedido"]["values"] = [
            pedido.id for pedido in self.pedidos
            if pedido.id not in con_despacho
        ]

    def actualizar_conductores(self):
        self.vista.selecciones["Conductor"]["values"] = [
            conductor.nombre for conductor in self.conductores
        ]

    def actualizar_vehiculos(self):
        self.vista.selecciones["Vehiculo"]["values"] = [
            vehiculo.patente for vehiculo in self.vehiculos
        ]

    def asignar_despacho(self):
        try:
            id_pedido = self.vista.selecciones["Pedido"].get()
            nombre_conductor = self.vista.selecciones["Conductor"].get()
            patente = self.vista.selecciones["Vehiculo"].get()

            pedido = next(
                (p for p in self.pedidos if p.id == id_pedido),
                None
            )

            conductor = next(
                (
                    c for c in self.conductores
                    if c.nombre == nombre_conductor
                ),
                None
            )

            vehiculo = next(
                (v for v in self.vehiculos if v.patente == patente),
                None
            )

            if pedido is None or conductor is None or vehiculo is None:
                raise ReglaNegocioError(
                    "Seleccione todos los datos del despacho"
                )

            if any(d.pedido.id == pedido.id for d in self.despachos):
                raise ReglaNegocioError(
                    "El pedido ya tiene un despacho asignado"
                )

            id_despacho = f"DES-{len(self.despachos) + 1}"

            despacho = Despacho(
                id_despacho,
                pedido,
                conductor,
                vehiculo
            )

            self.despachos.append(despacho)
            self.guardar_despachos()

            self.insertar_despacho_en_tabla(despacho)

            # El pedido ya no debe poder elegirse de nuevo
            self.actualizar_pedidos()
            self.vista.selecciones["Pedido"].set("")

            messagebox.showinfo(
                "Despacho asignado",
                f"Se asigno el despacho {id_despacho}"
            )

        except ReglaNegocioError as error:
            messagebox.showerror("Error", str(error))
