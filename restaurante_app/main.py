import tkinter as tk
from pathlib import Path

from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


RUTA_DATOS = Path(__file__).parent / "datos"


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Restaurante")
        self.ventana.geometry("1000x650")
        self.ventana.minsize(900, 600)

        archivo_servicio = ArchivoServicio(
            RUTA_DATOS
        )

        productos_datos = (
            archivo_servicio.cargar_productos()
        )

        usuarios_datos = (
            archivo_servicio.cargar_usuarios()
        )

        ventas_datos = (
            archivo_servicio.cargar_ventas()
        )

        self.restaurante_servicio = (
            RestauranteServicio(
                productos_datos,
                usuarios_datos,
                ventas_datos,
                archivo_servicio
            )
        )

        self.vista_actual = None
        self.usuario_autenticado = None

        self.mostrar_login()

    def limpiar_vista(self):
        if self.vista_actual is not None:
            self.vista_actual.destruir()

    def mostrar_login(self):
        self.limpiar_vista()

        self.usuario_autenticado = None

        self.vista_actual = LoginView(
            self.ventana,
            self.restaurante_servicio,
            self.mostrar_main
        )

    def mostrar_main(self, usuario_autenticado):
        self.limpiar_vista()

        self.usuario_autenticado = usuario_autenticado

        self.vista_actual = MainView(
            self.ventana,
            self.restaurante_servicio,
            self.mostrar_login,
            self.usuario_autenticado
        )

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.ejecutar()