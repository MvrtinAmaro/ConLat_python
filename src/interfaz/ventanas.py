import tkinter as tk
from tkinter import ttk


class VistaClientes:

    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = ttk.Label(
            self.frame,
            text="Gestion de Clientes",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        formulario = ttk.LabelFrame(
            self.frame,
            text="Datos del cliente",
            padding=15
        )
        formulario.pack(fill="x", padx=20, pady=10)

        campos = ["RUT", "Nombre", "Direccion", "Correo", "Telefono"]

        self.entradas = {}

        for i, campo in enumerate(campos):
            ttk.Label(formulario, text=campo).grid(
                row=i, column=0, padx=10, pady=5, sticky="w"
            )

            entrada = ttk.Entry(formulario, width=35)
            entrada.grid(row=i, column=1, padx=10, pady=5)

            self.entradas[campo] = entrada

        self.boton_registrar = ttk.Button(
            formulario,
            text="Registrar cliente"
        )
        self.boton_registrar.grid(
            row=5, column=1, pady=10, sticky="e"
        )

        columnas = ("rut", "nombre", "direccion", "correo", "telefono")

        self.tabla = ttk.Treeview(
            self.frame,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "rut": "RUT",
            "nombre": "Nombre",
            "direccion": "Direccion",
            "correo": "Correo",
            "telefono": "Telefono"
        }

        for columna in columnas:
            self.tabla.heading(
                columna,
                text=encabezados[columna]
            )
            self.tabla.column(columna, width=130)

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )


class VistaInventario:

    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = ttk.Label(
            self.frame,
            text="Gestion de Inventario",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        formulario = ttk.LabelFrame(
            self.frame,
            text="Datos del producto",
            padding=15
        )
        formulario.pack(fill="x", padx=20, pady=10)

        campos = [
            "ID",
            "Nombre",
            "Precio",
            "Cantidad disponible",
            "Stock minimo",
            "Peso por unidad (kg)"
        ]

        self.entradas = {}

        for i, campo in enumerate(campos):
            ttk.Label(formulario, text=campo).grid(
                row=i, column=0, padx=10, pady=5, sticky="w"
            )

            entrada = ttk.Entry(formulario, width=30)
            entrada.grid(row=i, column=1, padx=10, pady=5)

            self.entradas[campo] = entrada

        self.refrigeracion = tk.BooleanVar(value=False)

        ttk.Checkbutton(
            formulario,
            text="Requiere refrigeracion",
            variable=self.refrigeracion
        ).grid(
            row=6, column=1, padx=10, pady=5, sticky="w"
        )

        self.boton_registrar = ttk.Button(
            formulario,
            text="Registrar producto"
        )
        self.boton_registrar.grid(
            row=7, column=1, pady=10, sticky="e"
        )

        columnas = (
            "id", "nombre", "precio", "stock",
            "minimo", "peso", "refrigeracion"
        )

        self.tabla = ttk.Treeview(
            self.frame,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "id": "ID",
            "nombre": "Producto",
            "precio": "Precio",
            "stock": "Stock",
            "minimo": "Stock minimo",
            "peso": "Peso (kg)",
            "refrigeracion": "Refrigeracion"
        }

        for columna in columnas:
            self.tabla.heading(
                columna,
                text=encabezados[columna]
            )
            self.tabla.column(columna, width=105)

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )


class VistaPedidos:

    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = ttk.Label(
            self.frame,
            text="Gestion de Pedidos",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        formulario = ttk.LabelFrame(
            self.frame,
            text="Crear pedido",
            padding=15
        )
        formulario.pack(fill="x", padx=20, pady=10)

        ttk.Label(formulario, text="Cliente:").grid(
            row=0, column=0, padx=10, pady=8, sticky="w"
        )

        self.cliente = ttk.Combobox(
            formulario,
            width=30,
            state="readonly"
        )
        self.cliente.grid(
            row=0, column=1, padx=10, pady=8
        )

        ttk.Label(formulario, text="Producto:").grid(
            row=1, column=0, padx=10, pady=8, sticky="w"
        )

        self.producto = ttk.Combobox(
            formulario,
            width=30,
            state="readonly"
        )
        self.producto.grid(
            row=1, column=1, padx=10, pady=8
        )

        ttk.Label(formulario, text="Cantidad:").grid(
            row=2, column=0, padx=10, pady=8, sticky="w"
        )

        self.cantidad = ttk.Entry(
            formulario,
            width=33
        )
        self.cantidad.grid(
            row=2, column=1, padx=10, pady=8
        )

        self.boton_agregar = ttk.Button(
            formulario,
            text="Agregar producto"
        )
        self.boton_agregar.grid(
            row=3, column=1, pady=10, sticky="e"
        )

        columnas = (
            "producto",
            "cantidad",
            "precio",
            "subtotal"
        )

        self.tabla = ttk.Treeview(
            self.frame,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "producto": "Producto",
            "cantidad": "Cantidad",
            "precio": "Precio unitario",
            "subtotal": "Subtotal"
        }

        for columna in columnas:
            self.tabla.heading(
                columna,
                text=encabezados[columna]
            )
            self.tabla.column(columna, width=150)

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.total = ttk.Label(
            self.frame,
            text="Total del pedido: $0",
            font=("Arial", 14, "bold")
        )
        self.total.pack(pady=10)

        self.boton_crear = ttk.Button(
            self.frame,
            text="Crear pedido"
        )
        self.boton_crear.pack(pady=10)


class VistaDespachos:

    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = ttk.Label(
            self.frame,
            text="Gestion de Despachos",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        formulario = ttk.LabelFrame(
            self.frame,
            text="Asignar despacho",
            padding=15
        )
        formulario.pack(fill="x", padx=20, pady=10)

        campos = ["Pedido", "Conductor", "Vehiculo"]

        self.selecciones = {}

        for i, campo in enumerate(campos):
            ttk.Label(
                formulario,
                text=campo + ":"
            ).grid(
                row=i, column=0, padx=10, pady=8, sticky="w"
            )

            seleccion = ttk.Combobox(
                formulario,
                width=30,
                state="readonly"
            )

            seleccion.grid(
                row=i, column=1, padx=10, pady=8
            )

            self.selecciones[campo] = seleccion

        self.boton_asignar = ttk.Button(
            formulario,
            text="Asignar despacho"
        )
        self.boton_asignar.grid(
            row=3, column=1, pady=10, sticky="e"
        )

        columnas = (
            "id",
            "pedido",
            "conductor",
            "vehiculo",
            "estado"
        )

        self.tabla = ttk.Treeview(
            self.frame,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "id": "ID",
            "pedido": "Pedido",
            "conductor": "Conductor",
            "vehiculo": "Vehiculo",
            "estado": "Estado"
        }

        for columna in columnas:
            self.tabla.heading(
                columna,
                text=encabezados[columna]
            )
            self.tabla.column(columna, width=130)

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )
