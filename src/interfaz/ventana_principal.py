
import tkinter as tk
from tkinter import ttk, messagebox

from interfaz.ventanas import (
    VistaClientes,
    VistaInventario,
    VistaPedidos,
    VistaDespachos
)

from controlador.controladores import (
    ControladorClientes,
    ControladorInventario,
    ControladorPedidos,
    ControladorDespachos
)


class VentanaPrincipal:

    def __init__(self, clientes, productos, pedidos, conductores,
                 vehiculos, despachos):

        self.clientes = clientes
        self.productos = productos
        self.pedidos = pedidos
        self.conductores = conductores
        self.vehiculos = vehiculos
        self.despachos = despachos

        self.ventana = tk.Tk()
        self.ventana.title("CONLAT - Sistema de Gestion")
        self.ventana.geometry("1000x700")
        self.ventana.resizable(False, False)
        self.ventana.report_callback_exception = self.mostrar_error_inesperado

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = ttk.Label(
            self.ventana,
            text="CONLAT",
            font=("Arial", 24, "bold")
        )
        titulo.pack(pady=15)

        subtitulo = ttk.Label(
            self.ventana,
            text="Sistema de gestion de bodega y despachos"
        )
        subtitulo.pack()

        menu = ttk.Frame(self.ventana)
        menu.pack(pady=15)

        botones = [
            ("Inicio", self.mostrar_inicio),
            ("Clientes", self.mostrar_clientes),
            ("Inventario", self.mostrar_inventario),
            ("Pedidos", self.mostrar_pedidos),
            ("Despachos", self.mostrar_despachos)
        ]

        for i, (nombre, comando) in enumerate(botones):
            boton = ttk.Button(
                menu,
                text=nombre,
                width=17,
                command=comando
            )
            boton.grid(row=0, column=i, padx=5, pady=10)

        self.contenido = ttk.Frame(self.ventana)
        self.contenido.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.mostrar_inicio()

    def mostrar_error_inesperado(self, tipo, valor, traza):
        # tkinter solo imprime estos errores en consola; asi el usuario los ve
        import traceback
        traceback.print_exception(tipo, valor, traza)
        messagebox.showerror(
            "Error inesperado",
            f"{tipo.__name__}: {valor}"
        )

    def limpiar_contenido(self):
        for elemento in self.contenido.winfo_children():
            elemento.destroy()

    def mostrar_inicio(self):
        self.limpiar_contenido()

        ttk.Label(
            self.contenido,
            text="Bienvenido al sistema CONLAT",
            font=("Arial", 18)
        ).pack(pady=50)

        ttk.Label(
            self.contenido,
            text="Seleccione un modulo para comenzar."
        ).pack()

    def mostrar_clientes(self):
        self.limpiar_contenido()

        vista = VistaClientes(self.contenido)
        vista.frame.pack(fill="both", expand=True)

        ControladorClientes(vista, self.clientes)

    def mostrar_inventario(self):
        self.limpiar_contenido()

        vista = VistaInventario(self.contenido)
        vista.frame.pack(fill="both", expand=True)

        ControladorInventario(vista, self.productos)

    def mostrar_pedidos(self):
        self.limpiar_contenido()

        vista = VistaPedidos(self.contenido)
        vista.frame.pack(fill="both", expand=True)

        ControladorPedidos(
            vista,
            self.clientes,
            self.productos,
            self.pedidos
        )

    def mostrar_despachos(self):
        self.limpiar_contenido()

        vista = VistaDespachos(self.contenido)
        vista.frame.pack(fill="both", expand=True)

        ControladorDespachos(
            vista,
            self.pedidos,
            self.conductores,
            self.vehiculos,
            self.despachos
        )

    def iniciar(self):
        self.ventana.mainloop()
